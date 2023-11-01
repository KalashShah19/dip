#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:01:55 2023

@author: bmiit202006100110040
"""
import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate the minimum and maximum pixel values
min_value = np.min(image)
max_value = np.max(image)

# Apply range normalization
normalized_image = (image - min_value) / (max_value - min_value)

# Display or save the normalized image
cv2.imshow('Normalized Image', normalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
