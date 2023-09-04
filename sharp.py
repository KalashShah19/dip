#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 17:03:22 2023

@author: bmiit202006100110040
"""

import numpy as np
import cv2 as cv

img = cv.imread('img.jpeg')
cv.imshow('Original', img)

kernel = np.ones((3,3),np.float32)/9
dst = cv.filter2D(img,-1,kernel)

cv.imshow('Blurred', dst)
sharpen_filter = np.array([[0, -1, 0], 
                           [-1, 5, -1],
                           [0, -1, 0]])
sharpened = cv.filter2D(dst, -1, sharpen_filter)

cv.imshow('Sharpened', sharpened)
cv.imwrite('Sharpened.jpg', sharpened)
cv.waitKey(0)
cv.destroyAllWindows()