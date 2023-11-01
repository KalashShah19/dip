#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:15:49 2023

@author: bmiit202006100110040
"""

import cv2
import numpy as np

# Load the image
image = cv2.imread('input.jpg')

# Define the conservative smoothing kernel
kernel = np.array([[1, 2, 1],
                  [2, 4, 2],
                  [1, 2, 1]], dtype=np.float32) / 16

# Apply conservative smoothing
smoothed_image = cv2.filter2D(image, -1, kernel)

# Display the original and smoothed images
cv2.imshow('Original Image', image)
cv2.imshow('Conservative Smoothing', smoothed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
