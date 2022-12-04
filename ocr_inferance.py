#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
import cv2
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from augumentation import *

#importing the PADDLE OCR
from paddleocr import PaddleOCR
ocr = PaddleOCR(lang='en',rec_algorithm='CRNN')

#### input the image with path below
#input_image = input()

def get_image(ab):
    input_image = ab
    # Reading image 
    img = cv2.imread(input_image)

    # Preprocess image 
    gray = get_grayscale(img)
    thresh = thresholding(gray)
    opg = opening(gray)
    cnny = canny(gray)
    images = {'gray': gray, 
            'thresh': thresh, 
            'opening': opg, 
            'canny': cnny}
    image = np.expand_dims(img,0)

    return img, image

#savedModel= tf.keras.models.load_model(r"C:\Users\dell\Music\OCR_classification\best_model.h5")
#print(savedModel.summary())

def prediction(image):
    # load model
    savedModel= tf.keras.models.load_model(r"C:\Users\dell\Music\OCR_classification\best_model.h5")
    x = savedModel.predict(image)

    #print(x)

    class_names = ['not receipt', 'receipt']
    return class_names[np.argmax(x[0])]


# Detect texts from image
def text_extraction(image,img):
    if prediction(image) == 'receipt':
        print("Its a receipt" +"\n" + '*'*80)
        texts = ocr.ocr(img)
        for i in texts:
            for j in i:
                print(j[1][0], end=", ")
            print("")
    else:
        print("It's not a receipt. please upload receipt")