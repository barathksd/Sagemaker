

# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 19:40:54 2021

@author: Lenovo
"""

from zipfile import ZipFile
import numpy as np
import pandas as pd
import os
import argparse

'''
https://www.kaggle.com/mustafacicek/imdb-top-250-lists-1996-2020
https://drive.google.com/file/d/1onNp_5ixFFshiVh463AS2yt7so5KWdjG/view?usp=sharing
Index(['Ranking', 'IMDByear', 'IMDBlink', 'Title', 'Date', 'RunTime', 'Genre',
       'Rating', 'Score', 'Votes', 'Gross', 'Director', 'Cast1', 'Cast2',
       'Cast3', 'Cast4'],
      dtype='object')
'''

def get_df(input_path,drop_duplicates='False'):
    input_path = input_path.replace('/','\\')
    zip_path = input_path[:input_path.rfind('\\')]
    csv_file = input_path[len(zip_path)+1:]
    columns = ['Ranking', 'IMDByear', 'IMDBlink', 'Title', 'Date', 'RunTime', 'Genre',
       'Rating', 'Score', 'Votes', 'Gross', 'Director', 'Cast1', 'Cast2',
       'Cast3', 'Cast4']
    with ZipFile(zip_path, 'r') as z:
        # printing all the contents of the zip file
        df = pd.read_csv(z.open(csv_file)) 
    if drop_duplicates:
        df = df.drop_duplicates('Title').reset_index(drop=True)
    
    i = columns.index('Gross')
    columns = [columns[i]]+columns[:i]+columns[i+1:]
    df = df[columns]
    return df

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    #parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])

    args = parser.parse_args()
    base = '/opt/ml/processing/input'
    #base2 = r'C:\Users\Lenovo\Downloads\imdbTop250.csv.zip'

    csv_file = 'imdbTop250.csv'
    input_path = os.path.join(base,csv_file)
    df = get_df(input_path,drop_duplicates=True)
    
    df_nan = df['Gross'].apply(np.isnan)
    df_test = df[df_nan == True].reset_index(drop=True)
    df_train = df[df_nan == False]
    df_train = df_train.sample(frac=1).reset_index(drop=True)
    df_nan = None
    
    train_output_path = os.path.join("/opt/ml/processing/fulltrain", "train.csv")
    test_output_path = os.path.join("/opt/ml/processing/test", "test.csv")
    
    df_train.to_csv(train_output_path,header=None,index=False)
    df_test.to_csv(test_output_path,header=None,index=False)
    
