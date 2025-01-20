import os
import sys

import boto3
import dill
import numpy as np
import pandas as pd
import yaml
from pymongo import MongoClient

from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


from src.exception import CustomException

def read_yaml_file(filename:str)-> dict:
    try:
        with open(filename,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CustomException (e,sys) from e 
    
def export_collection_as_dataframe(collection_name ,db_name):
    try:
        mongo_client = MongoClient(os.getenv('MONGO_dB_URL'))
        collection = mongo_client[db_name][collection_name]
        df = pd.DataFrame(list(collection.find()))

        if "_id" in df.columns.to_list():
            df = df.drop(columns=['_id'],axis=1)

        df.replace({'na':np.nan},inplace=True)

        return df 
    except Exception as e:
        raise CustomException (e,sys)