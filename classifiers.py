''' Import Libraries'''
import pandas as pd
import numpy as np


class Classifier:
    ''' This is a class prototype for any classifier. It contains two empty methods: predict, fit'''
    def __init__(self):
        self.model_params = {}
        pass
    
    def predict(self, x):
        '''This method takes in x (numpy array) and returns a prediction y'''
        raise NotImplementedError
    
    def fit(self, x, y):
        '''This method is used for fitting a model to data: x, y'''
        raise NotImplementedError



            
class Prior(Classifier):
    
    def __init__(self):
        ''' Your code here '''
        self.model_params = {}
        pass
    
    def predict(self, x):
        '''This method takes in x (numpy array) and returns a prediction y'''
        if not self.model_params:
            raise ValueError("The model has not been fitted yet. Call fit() before predict().")

        decision_label = None
        max_value = float('-inf')
        for key, value in self.model_params.items():
            if value > max_value:
                max_value = value
                decision_label = key
        return [decision_label] * len(x)
        
    
    
    def fit(self, x, y):
        '''This method is used for fitting a model to data: x (numpy array), y (numpy array)'''
        label_counts = {}
        for label in y:
            label_counts[label] = label_counts.get(label, 0) + 1
        n_samples = len(y)
        for label,count in label_counts.items():
            self.model_params[label] = count / n_samples 
        
        
        
