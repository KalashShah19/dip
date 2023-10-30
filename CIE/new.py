#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:41:58 2023

@author: exam029
"""

import cv2 
import numpy as np

# read the image 
img = cv2.imread("8.jpg", 0) 

# binarize the image 
binary_image = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1] 
inv = cv2.bitwise_not(binary_image)
cv2.imshow('8', inv)
cv2.waitKey(0)
cv2.destroyAllWindows()
