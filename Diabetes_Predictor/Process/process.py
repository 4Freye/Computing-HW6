import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from abc import ABCMeta, abstractmethod
from itertools import compress

#b
class PreProcess:
    def drop_na(df, cols):
        return df.dropna(subset = cols, axis=0)

#train = PreProcess.drop_na(train, ['age','gender','ethnicity'])
#test = PreProcess.drop_na(test, ['age','gender','ethnicity'])

#c
class PreProcessFill:
    def fill_na(df, cols):
        return df.apply(lambda x: x.fillna(x.mean()) if x.name in cols else x)

#train = PreProcessFill.fill_na(train, ['height','weight'])
#test = PreProcessFill.fill_na(test, ['height','weight'])

#train.dropna(inplace=True, axis=0)
#test.dropna(inplace=True, axis=0)


#d. Create at least two feature classes that transform some of the columns in the data set. 
# These feature classes need to have the same structure defined by an abstract parent class (Remember: polymorphism).

class FeatureCreate:
    @abstractmethod
    def create_feature():
        pass

class interact(FeatureCreate):
    def create_feature(df, col1 : int or float, col2 : int or float):
        df[col1 + col2] = df[col1] * df[col2]
        return df

class dummify(FeatureCreate):
    def create_feature(df):
        string_cols = list(compress(list(df.columns.values), [isinstance(s, str) for s in df.iloc[0,:]]))
        df = pd.get_dummies(df,  columns = string_cols)
        return df

class concat(FeatureCreate):
    def create_feature(df, col1: str, col2:str):
        df[col1 + col2] = df.agg(lambda x: f"{x[col1]} {x[col2]}", axis=1)
        return df

#train = concat.create_feature(train, 'ethnicity','gender')
#train = interact.create_feature(train, 'height','weight')
#test = concat.create_feature(test, 'ethnicity','gender')
#test = interact.create_feature(test, 'height','weight')

#train = dummify.create_dummies(train).columns.values
#test = dummify.create_dummies(test).columns.values
