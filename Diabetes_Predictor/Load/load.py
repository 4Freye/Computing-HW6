import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from abc import ABCMeta, abstractmethod
from itertools import compress

#a
class LoadData:
    def __init__(self, path_df):
        self.dataset = pd.read_csv(path_df)
        self.dependent = self.dataset.iloc[:,-1]
        self.independent = self.dataset.iloc[:,:-1]

    def split(self, seed):
        self.independent = dummify.create_dummies(self.independent)
        X_train, X_test, y_train, y_test =  train_test_split(self.independent, self.dependent, random_state=seed)
        train = pd.concat([X_train, y_train], axis=1)
        test = pd.concat([X_test, y_test], axis=1)
        return train, test

#loaddata1 = LoadData('/Users/ericfrey/Documents/computing/Computing-HW6/sample_diabetes_mellitus_data.csv')
#train, test = loaddata1.split(seed= 1)