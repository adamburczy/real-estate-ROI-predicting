import pickle
import json
import numpy as np

global __model
with open('model.pickle', 'rb') as f:
    __model = pickle.load(f)

def get_estimated_price(Price, Rooms):
    x = np.zeros(2)
    x[0] = Price
    x[1] = Rooms

    return round(__model.predict([x])[0],2)

if __name__ == '__main__':
    print(get_estimated_price(300000,2))
    print(get_estimated_price(421000,4))