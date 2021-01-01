import pickle
import numpy as np
import json
import os

__data_columns = None
__model = None

def predict_roi(Price, Rooms):
    x = np.zeros(len(__data_columns))
    x[0] = Price
    x[1] = Rooms
    return round(__model.predict([x])[0], 2)

def load_model():
    print('loading model...')
with open('columns.json') as f:
    __data_columns = json.load(f)['data_columns']

with open('model.pickle', 'rb') as f:
    __model = pickle.load(f)
    print('loading model done')


print(predict_price(300000, 3))