# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 12:07:55 2021

@author: Lenovo
"""

from zipfile import ZipFile
import os
import pickle
import string
import argparse
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import io

def to_libsvm(f, labels, values):
    f.write(
        bytes(
            "\n".join(
                [
                    "{} {}".format(
                        label, " ".join(["{}:{}".format(i + 1, el) for i, el in enumerate(vec)])
                    )
                    for label, vec in zip(labels, values)
                ]
            ),
            "utf-8",
        )
    )
    return f



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    args = parser.parse_args()
    base = '/opt/ml/processing/input'
    #base = r'C:\Users\Lenovo\Desktop\data\code\datasets'
    rbase = "/opt/ml/processing/output"
    
    df = pd.read_csv(base+'/iris.csv', sep=",",header=None)
    df = df.sample(frac = 1).reset_index(drop=True)
    df.columns = ['SEPAL LENGTH','SEPAL WIDTH','PETAL LENGTH','PETAL WIDTH','class']

    d = {i:index for index,i in enumerate(np.sort(df['class'].unique()))}
    df['class'] = df['class'].map(lambda x: d[x])


    xtrain,xtest,ytrain,ytest = train_test_split(df.iloc[:,:-1],df['class'],test_size=0.2)
    s = [('train',xtrain,ytrain),('test',xtest,ytest)]
    
    for name,x,y in s:
        key = 'iris_'+name
        f = io.BytesIO()
        to_libsvm(
                    f,
                    y.values,
                    x.values,
                )
        f.seek(0)
        
        with open(os.path.join(rbase,key),'wb') as g:
            g.write(f.read())