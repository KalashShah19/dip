#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:07:41 2023

@author: bmiit202006100110040
"""

# import required libraries
import cv2
import numpy as np

# Read an input image as a gray image
img = cv2.imread('pt.jpg')

# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:250, 150:450] = 255

# compute the bitwise AND using the mask
masked_img = cv2.bitwise_and(img,img,mask = mask)

# display the mask, and the output image
cv2.imshow('Mask',mask)
cv2.imshow('Masked Image',masked_img)
cv2.waitKey(0)
cv2.destroyAllWindows()