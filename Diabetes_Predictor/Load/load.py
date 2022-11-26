import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from abc import ABCMeta, abstractmethod
from itertools import compress

#a
class LoadData:
    def __init__(self, path_df):
        if isinstance(path_df, str):
            self.dataset = pd.read_csv(path_df)
        else:
            self.dataset = path_df
        
        target = 'diabetes_mellitus'
        features = self.dataset.columns.values[[x != target for x in self.dataset.columns.values]]
        self.dependent = self.dataset[target]
        self.independent = self.dataset[features]

    def create_df(self):
        return self.dataset

    def split(self, seed):
        X_train, X_test, y_train, y_test =  train_test_split(self.independent, self.dependent, random_state=seed)
        train = pd.concat([X_train, y_train], axis=1)
        test = pd.concat([X_test, y_test], axis=1)
        return train, test