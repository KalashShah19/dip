#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:23:47 2023

@author: bmiit202006100110040
"""

import cv2
import numpy as np

# Load the binary image
binary_image = cv2.imread('binary_image.jpg', cv2.IMREAD_GRAYSCALE)

# Define a kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)  # You can adjust the kernel size

# Perform dilation
dilated_image = cv2.dilate(binary_image, kernel, iterations=1)

# Perform erosion
eroded_image = cv2.erode(binary_image, kernel, iterations=1)

# Perform opening (erosion followed by dilation)
opening_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)

# Perform closing (dilation followed by erosion)
closing_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

# Display the original and processed images
cv2.imshow('Original Binary Image', binary_image)
cv2.imshow('Dilated Image', dilated_image)
cv2.imshow('Eroded Image', eroded_image)
cv2.imshow('Opening Image', opening_image)
cv2.imshow('Closing Image', closing_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
