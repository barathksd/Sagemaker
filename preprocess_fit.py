# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 13:43:09 2021

@author: Lenovo
"""

import os
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import MultiLabelBinarizer, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import joblib
import json
import argparse
from preprocess_common import get_df
from io import StringIO, BytesIO

from sagemaker_containers.beta.framework import (
    content_types, encoders, env, modules, transformer, worker)

#z_file = 
csv_file = 'imdbTop250.csv'

'''
https://www.kaggle.com/mustafacicek/imdb-top-250-lists-1996-2020
https://drive.google.com/file/d/1onNp_5ixFFshiVh463AS2yt7so5KWdjG/view?usp=sharing
Index(['Ranking', 'IMDByear', 'IMDBlink', 'Title', 'Date', 'RunTime', 'Genre',
       'Rating', 'Score', 'Votes', 'Gross', 'Director', 'Cast1', 'Cast2',
       'Cast3', 'Cast4'],
      dtype='object')
'''

columns = ['Gross', 'Ranking', 'IMDByear', 'IMDBlink', 'Title', 'Date', 'RunTime', 'Genre',
   'Rating', 'Score', 'Votes', 'Director', 'Cast1', 'Cast2',
   'Cast3', 'Cast4']
genre_features = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy','Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir','History', 'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi','Short', 'Sport', 'Thriller', 'War', 'Western']


def column_process(df):
    df[df.columns[12:]] = df[df.columns[12:]].fillna('NaN').applymap(lambda x: x.strip())
    cast = df[df.columns[12:]].values
    cast = cast.reshape(-1,).astype('U')
    cast = pd.Series(cast)
    cast_vc = cast.value_counts()
    cast_vc['NaN'] = 0
    m = cast_vc.max()
    df['Cast'] = df[df.columns[12:]].applymap(dict(cast_vc).get).sum(axis=1)/m
    df = df.drop(columns=['Title','Ranking','IMDByear','IMDBlink','Cast1','Cast2','Cast3','Cast4'])
    
    director_vc = df['Director'].value_counts()
    m = director_vc.max()
    df['Director'] = df['Director'].apply(dict(director_vc).get)/m
    
    mean = np.round((df['Score']/df['Rating']).dropna().mean(),3)
    df_nan = df['Score'].apply(np.isnan)
    df.loc[df_nan,'Score'] = (df.loc[df_nan,'Rating']*mean).values
    return df

def genre_process(df,genre_features):
    mlb = MultiLabelBinarizer(classes=genre_features)
    genre = df['Genre'].apply(lambda x: x.replace(' ','')).values
    l = [i.split(',') for i in genre]
    garray = mlb.fit_transform(l)
    genre_list = mlb.classes_.astype('U')
    garray = pd.DataFrame(garray,columns=genre_list)
    df = df.drop(columns=['Genre'])
    
    return pd.concat([df,garray],axis=1)
    
def input_fn(input_path, content_type='zip'):

    if content_type == 'text/csv':
        # Read the raw input data as CSV.
        df = pd.read_csv(StringIO(input_path), 
                         header=None)
        
    elif content_type == 'csv':
        df = pd.read_csv(input_path,
                         header=None)
        
    elif content_type == 'zip':
        input_path = input_path.replace('/','\\')
        zip_path = input_path[:input_path.rfind('\\')]
        csv_file = input_path[len(zip_path)+1:]
        df = get_df(zip_path,csv_file)
        
    else:
        raise Exception("Invalid content type")
    
    df.columns = columns
    
    df = column_process(df)
    df = genre_process(df,genre_features)
    print(df.head())
    return df
    

def save_model(model,model_dir):
    if not os.path.exists(model_dir):
        os.mkdir(model_dir)
    joblib.dump(model, os.path.join(model_dir,"model.joblib"))
    
def model_fn(model_dir):
    return joblib.load(os.path.join(model_dir, "model.joblib"))

def fit_model(model_dir,df,genre_features,n_components=16):
    numeric_features = ['Date', 'RunTime', 'Rating', 'Score', 'Votes', 'Director', 'Cast']
    numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())])
        
    n_components = 16
    model = PCA(n_components=n_components)
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', model, genre_features)])

    preprocessor.fit(df)
    
    save_model(preprocessor,model_dir)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])
    
    args = parser.parse_args()
                  
    df = input_fn(os.path.join(args.train,'train.csv'),content_type='csv')
    fit_model(args.model_dir,df,genre_features,n_components=16)
    
    
def predict_fn(input_data, model):

    return model.transform(input_data)


def output_fn(prediction, accept="application/json"):
    """Format prediction output

    The default accept/content-type between containers for serial inference is JSON.
    We also want to set the ContentType or mimetype as the same value as accept so the next
    container can read the response payload correctly.
    """
    if accept == "application/json":
        instances = []
        for row in prediction.tolist():
            instances.append({"features": row})

        json_output = {"instances": instances}
        #return json.dumps(json_output)
   
        return worker.Response(json.dumps(json_output), accept, mimetype=accept)
        
    elif accept == 'text/csv':
        return worker.Response(encoders.encode(prediction, accept), accept, mimetype=accept)
    else:
        raise Exception("{} accept type is not supported by this script.".format(accept))
    
    return

