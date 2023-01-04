import numpy as np
import cv2
import matplotlib.pyplot as plt
from keras.models import model_from_json

json = open('models/model.json', 'r')
model_json = json.read()
json.close()
model = model_from_json(model_json)
model.load_weights('models/model.h5')
print('Model Loaded')

def predict(image):
    image_resize = cv2.resize(image,(28,28))
    image_resize_2 = image_resize.reshape(1,1,28,28)
    pred = model.predict(image_resize_2)
    return (np.argmax(pred[0]))

def extract_numbers(sudoku):
    sudoku = cv2.resize(sudoku, (450,450))
    grid = np.zeros([9,9])
    for i in range(9):
        for j in range(9):
            image = sudoku[i*50:(i+1)*50, j*50:(j+1)*50]
            if image.sum()>100000:
                grid[i,j] = predict(image)
            else:
                grid[i,j] = 0
    return (grid.astype(int))