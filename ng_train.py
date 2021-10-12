# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 14:28:21 2021

@author: Lenovo
"""

import os
import joblib
import pickle
import argparse
import string
import random
import numpy as np
import torch
import torch.nn as nn
from torch.nn import functional as F
from sklearn.preprocessing import MultiLabelBinarizer

np.set_printoptions(precision=3)
all_letters = list(string.ascii_letters[:26]+" .,;'")+['<EOS>','<S>']
n_letters = len(all_letters)
MLB = MultiLabelBinarizer(classes=all_letters)
MLB.fit(all_letters)

#OHE = OneHotEncoder(categories=[np.array([i for i in all_letters])],handle_unknown='ignore')
#OHE.fit([[i] for i in all_letters])

def turnToTensor(name,mlb):
    return torch.FloatTensor(mlb.transform(list(name)))

    
def get_data(names,max_val=1000):
    a = {}
    for category,ns in names.items():
        ns = np.array(ns)
        np.random.shuffle(ns)
        ns = ns[:max_val]
        l = []
        for name in ns:
            l.append(([['<S>'],name[0]],name[1]))
            if len(name)>=2:
                l.extend([(name[:i],name[i]) for i in range(2,len(name))])
            l.append((name,'<EOS>'))
        a[category] = l
    return a


def get_sample(training_data):
    c = random.choice(all_categories)
    return random.choice(training_data[c]),c

class LSTMnamer(nn.Module):
    
    def __init__(self,in_size,hidden_size,out_size):
        super(LSTMnamer,self).__init__()
        self.hidden_size = hidden_size
        self.lstm = nn.LSTM(in_size,hidden_size)
        #self.lstm2 = nn.LSTM(hidden_size,hidden_size)
        self.linear = nn.Linear(hidden_size, out_size)
        self.out = nn.LogSoftmax(dim=1)
        self.hidden_cell = (torch.zeros(1,1,self.hidden_size),
                            torch.zeros(1,1,self.hidden_size))

    def forward(self,x):
        y,self.hidden_cell = self.lstm(x.view(len(x),1,-1),self.hidden_cell)
        #y,_ = self.lstm2(y.view(len(x),1,-1))
        y = self.linear(y.view(len(x),-1))
        y = self.out(y)
        return y[-1]
    
    def init_hidden(self):
        self.hidden_cell = (torch.zeros(1,1,self.hidden_size),
                            torch.zeros(1,1,self.hidden_size))


def train(opt,model,training_data):

    loss_function = opt['loss']
    optimizer = opt['optimizer']
    epochs = opt['epochs']
    loss_list = []
    for epoch in range(epochs):
        name, category = get_sample(training_data)
        category = turnToTensor([[category]], MLB2)
        inp,target = turnToTensor(name[0], MLB),torch.LongTensor([all_letters.index(name[1])])
        
        optimizer.zero_grad()
        model.init_hidden()

        out = model(torch.cat((torch.tile(category,(len(inp),1)),inp),axis=1))
        l = loss_function(out.view(1,-1), target)
        loss_list.append(l.item())
        #print(l,out.view(1,-1), category)
        l.backward()
        optimizer.step()

        if epoch%2000 == 0:
            print(f'epoch: {epoch} loss: {np.mean(loss_list):10.8f}')
            loss_list = []
    return model

#train(opt,model,training_data)

def save_skmodel(model,model_dir,model_name):
    if not os.path.exists(model_dir):
        os.mkdir(model_dir)
    joblib.dump(model, os.path.join(model_dir,model_name))

def load_skmodel(model_dir,model_name):
    return joblib.load(os.path.join(model_dir, model_name))

def save_model(model,model_dir):
    
    path = os.path.join(model_dir, "ng_model")
    # recommended way from http://pytorch.org/docs/master/notes/serialization.html
    torch.save(model.cpu().state_dict(), path)

def load_model(model_dir):
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    with open(os.path.join(model_dir, "ng_model"), "rb") as f:
        model.load_state_dict(torch.load(f))
    return model.to(device)
        
def get_output(out):
    return np.random.choice(np.arange(len(out)),p=torch.exp(out).detach().numpy())

def predict_fn(category,models):

    model = models['model']
    MLB = models['MLB']
    MLB2 = models['MLB2']
    if category is None:
        category = random.choice(all_categories)
    ct = turnToTensor([[category]], MLB2)
    name = ''
    inp = turnToTensor([['<S>']], MLB)
    i = 0
    model.init_hidden()
    while True:
        with torch.no_grad():
            out = model(torch.cat((torch.tile(ct,(len(inp),1)),inp),axis=1))
        out = get_output(out)
        if all_letters[out] == '<EOS>':
            break
        name += all_letters[out]
        inp = turnToTensor(all_letters[out], MLB)
        i += 1
        if i>20:
            break
        
    return name,category

def generate_count(category,count,models):
    
    for _ in range(count):
        print(predict_fn(category, models))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])
    parser.add_argument('--epochs', type=int, default=100000)
    parser.add_argument('--learning-rate', type=float, default=0.002)
    args = parser.parse_args()
    
    
    input_path = os.path.join(args.train,'processed_names')

    with open(input_path,'rb') as f:
        names = pickle.load(f)
        
    categories_dict = {index:i for index,i in enumerate(names.keys())}
    all_categories = list(names.keys())
    n_categories = len(all_categories)
    MLB2 = MultiLabelBinarizer(classes=all_categories)
    MLB2.fit([[i] for i in all_categories])
    training_data = get_data(names)
    #list(map(lambda x: (x[0],len(x[1])),training_data.items()))


    n_hidden = 128
    n_categories = len(names.keys())
    model = LSTMnamer(n_letters+n_categories,n_hidden,len(all_letters)-1)
    opt = {}
    opt['loss'] = nn.NLLLoss()  # negative log likelihood loss
    opt['optimizer'] = torch.optim.Adam(model.parameters(), lr=args.learning_rate)
    opt['epochs'] = args.epochs
    models = {}
    models['model'] = model
    models['MLB'] = MLB
    models['MLB2'] = MLB2
    
    generate_count('Japanese',10,models)
    
    model = train(opt,model,training_data)
    
    model_dir = args.model_dir
    model_name = 'ng_model'
    save_model(model, model_dir)
    #save_skmodel(MLB,model_dir,'MLB')
    #save_skmodel(MLB2,model_dir,'MLB2')
    
    generate_count('Japanese',10,models)

    
    
    


