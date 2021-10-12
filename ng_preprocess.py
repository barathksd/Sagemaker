# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 20:01:20 2021

@author: Lenovo
"""

from zipfile import ZipFile
import os
import pickle
import string
import argparse
import unicodedata
import numpy as np


np.set_printoptions(precision=3)

#OHE = OneHotEncoder(categories=[np.array([i for i in all_letters])],handle_unknown='ignore')
#OHE.fit([[i] for i in all_letters])

all_letters = list(string.ascii_letters[:26]+" .,;'")+['<EOS>','<S>']

def unicodeToAscii(s):
    s = s.strip()
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
        and c in all_letters
    )


def load_data(zip_path):
    with ZipFile(zip_path, 'r') as z:

        names = {}
        for i in z.filelist:
            with z.open(i) as f:
                n = f.read().strip().decode('utf-8').lower().split('\n')
            n = list(map(unicodeToAscii,n))
            names[i.filename.split('.')[0].split('/')[1]] = list(set(n))
            
        return names

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    args = parser.parse_args()
    base = '/opt/ml/processing/input'
    base_train = "/opt/ml/processing/train"
    zip_file = 'names.zip'
    input_path = os.path.join(base,zip_file)
    
    names = load_data(input_path)
    
    train_output_path = os.path.join(base_train, "processed_names")
    with open(train_output_path,'wb') as f:
        pickle.dump(names,f)

    
    
    
    