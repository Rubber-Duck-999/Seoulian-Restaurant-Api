import os
import random


class PredictionModel:
    a = 0
    b = 0 

    def __init__(self):
        self.a = 1
        self.b = 1

    def predict(self, testing_data):
        prediction = random.randint(0,50)
        return prediction

    def convert_to_json(self, df):
        return df.to_json()