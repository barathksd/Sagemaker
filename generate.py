# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 23:59:44 2021

@author: Lenovo
"""

import os
import json
import joblib
import pickle
import argparse
import unicodedata
import string
import random
import numpy as np
import torch
from ng_train import LSTMnamer, predict_fn, turnToTensor
from sklearn.preprocessing import MultiLabelBinarizer

JSON_CONTENT_TYPE = 'application/json'
all_letters = list(string.ascii_letters[:26]+" .,;'")+['<EOS>','<S>']
n_letters = len(all_letters)
MLB = MultiLabelBinarizer(classes=all_letters)
MLB.fit(all_letters)
all_categories = ['Arabic', 'Chinese', 'Czech', 'Dutch', 'English', 'French',
                  'German', 'Greek', 'Irish', 'Italian', 'Japanese', 'Korean',
                  'Polish', 'Portuguese', 'Russian', 'Scottish', 'Spanish',
                  'Vietnamese']
n_categories = len(all_categories)
MLB2 = MultiLabelBinarizer(classes=all_categories)
MLB2.fit([[i] for i in all_categories])

def input_fn(serialized_input_data, content_type=JSON_CONTENT_TYPE):

    if content_type == JSON_CONTENT_TYPE:
        input_data = json.loads(serialized_input_data)
        return input_data
    raise Exception('Requested unsupported ContentType in content_type: ' + content_type)
    
def load_skmodel(model_dir,model_name):
    return joblib.load(os.path.join(model_dir, model_name))

def load_model(model_dir):
    n_hidden = 128
    model = LSTMnamer(n_letters+n_categories,n_hidden,len(all_letters)-1)
    with open(os.path.join(model_dir, "ng_model"), "rb") as f:
        model.load_state_dict(torch.load(f))
    return model

def model_fn(model_dir):

    models = {}
    models['model'] = load_model(model_dir)
    models['MLB'] = MLB
    models['MLB2'] = MLB2
    return models

def output_fn(prediction_output, accept=JSON_CONTENT_TYPE):
    
    if accept == JSON_CONTENT_TYPE:
        return json.dumps(prediction_output), accept
    
    raise Exception('Requested unsupported ContentType in Accept: ' + accept)

