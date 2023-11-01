#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:44:23 2023

@author: bmiit202006100110040
"""

import cv2
import numpy as np

# Load the grayscale image
image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# a. Image negative
image_negative = 255 - image

# b. Log transformation
c = 255 / np.log(1 + np.max(image))
log_transformed = c * (np.log(image + 1))

# c. Power law transformation (Gamma correction)
gamma = 0.5  # You can adjust the gamma value
power_law_transformed = np.power(image, gamma)

# Display the original and transformed images
cv2.imshow('Original Image', image)
cv2.imshow('Image Negative', image_negative)
cv2.imshow('Log Transformation', log_transformed.astype(np.uint8))
cv2.imshow('Power Law Transformation', power_law_transformed.astype(np.uint8))

cv2.waitKey(0)
cv2.destroyAllWindows()
