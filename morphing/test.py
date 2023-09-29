#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 13:02:31 2023

@author: bmiit202006100110040
"""

# Python program to explain cv2.erode() method

# importing cv2
import cv2

# importing numpy
import numpy as np

# path
path = 'dots.png'

# Reading an image in default mode
img= cv2.imread(path,0)

thresh, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #binary
binary = cv2.bitwise_not(binary)  

# Window name in which image is displayed
window_name = 'Image'

# Creating kernel
kernel = np.ones((5, 5), np.uint8)

# Using cv2.erode() method
new = cv2.erode(binary, kernel)

# Displaying the image
cv2.imshow("OG", img)
cv2.imshow("New", new)
cv2.imshow("Binary", binary)

cv2.waitKey(0)

cv2.destroyAllWindows()
