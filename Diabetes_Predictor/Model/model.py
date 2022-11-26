import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from abc import ABCMeta, abstractmethod
from itertools import compress

#e and f
class Model:
    def __init__(self, features, target):
        self.features = features
        self.target = target
        #self.hyperparameter = max_depth
        self.model = RandomForestClassifier()
    
    def fit(self, df):
        self.model.fit(df.filter(items=self.features) , df[self.target])
        pass

    def predict(self, df):
        return self.model.predict_proba(df.filter(items = features))


#target = 'diabetes_mellitus'
#features = train.columns.values[[x != target for x in train.columns.values]]

#model1 = Model(features= features, target=target)

#model1.fit(train)
#model1.predict(test)

#string_cols = list(compress(list(train.columns.values), [isinstance(s, str) for s in train.iloc[0,:]]))
