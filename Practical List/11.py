#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:05:31 2023

@author: bmiit202006100110040
"""
import cv2

# Load the grayscale image
image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization
equalized_image = cv2.equalizeHist(image)

# Display the original and equalized images
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()