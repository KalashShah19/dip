#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 16:56:39 2023

@author: bmiit202006100110040
"""
import numpy as np
import cv2 as cv

img = cv.imread('1.jpg')
cv.imshow('Original', img)
kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)
cv.imshow('Blurred', dst)
cv.waitKey(0)
cv.destroyAllWindows()