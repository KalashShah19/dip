#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 16:53:36 2023

@author: bmiit202006100110040
"""

import cv2
import numpy as np

image = cv2.imread('img.jpeg')
cv2.imshow('Original', image)
sharpen_filter = np.array([[0, -1, 0], 
                           [-1, 5, -1],
                           [0, -1, 0]])
sharpened = cv2.filter2D(image, -1, sharpen_filter)
cv2.imshow('Image Sharpening', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()