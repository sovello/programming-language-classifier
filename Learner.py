import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

class Learner(object):
    '''Takes a dataframe with outcomes on first column and predictor second column
    Makes available the score and predict methods
    '''
    def __init__(self, dataframe, alg='NBayes'):
        self.outcome, self.predictor = self.split_data(dataframe)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.predictor, self.outcome)
        
        self.pipe = Pipeline([('bag_of_words', CountVectorizer()),
                                                              ('bayes', MultinomialNB())])
        self.fit()

        
    def fit(self):
        self.pipe.fit(self.X_train, self.y_train)

        
    def test_score(self):
        return self.pipe.score(self.X_test, self.y_test)

    
    def train_score(self):
        return self.pipe.score(self.X_train, self.y_train)

    
    def predict(self, string):
        return self.pipe.predict([string])


    def split_data(self, data):
        return data.loc[:,0], data.loc[:,1]
