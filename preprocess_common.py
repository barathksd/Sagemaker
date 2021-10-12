

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 13:57:59 2021

@author: Lenovo
"""

from zipfile import ZipFile
import numpy as np
import pandas as pd


'''
https://www.kaggle.com/mustafacicek/imdb-top-250-lists-1996-2020
https://drive.google.com/file/d/1onNp_5ixFFshiVh463AS2yt7so5KWdjG/view?usp=sharing
Index(['Ranking', 'IMDByear', 'IMDBlink', 'Title', 'Date', 'RunTime', 'Genre',
       'Rating', 'Score', 'Votes', 'Gross', 'Director', 'Cast1', 'Cast2',
       'Cast3', 'Cast4'],
      dtype='object')
'''

def get_df(zip_path,csv_file,drop_duplicates='False'):

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

