#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:06:55 2023

@author: bmiit202006100110040
"""

import cv2
import numpy as np

# Load the image
image = cv2.imread('input.jpg')

# Define the kernel size for the averaging filters
kernel_size = 5

# Create the standard averaging kernel
standard_kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)

# Create a custom weighted averaging kernel (e.g., emphasis on center pixel)
weighted_kernel = np.array([
    [0.01, 0.1, 0.01],
    [0.1, 2.0, 0.1],
    [0.01, 0.1, 0.01]
], dtype=np.float32)

# Apply standard averaging
standard_avg_image = cv2.filter2D(image, -1, standard_kernel)

# Apply weighted averaging
weighted_avg_image = cv2.filter2D(image, -1, weighted_kernel)

# Display the original, standard-averaged, and weighted-averaged images
cv2.imshow('Original Image', image)
cv2.imshow('Standard Averaged Image', standard_avg_image)
cv2.imshow('Weighted Averaged Image', weighted_avg_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
