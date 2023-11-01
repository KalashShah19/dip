#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:07:33 2023

@author: bmiit202006100110040
"""

import cv2

# Load the image
image = cv2.imread('input.jpg')

# Define mask sizes
mask_sizes = [3, 5, 7, 13, 25]

# Apply blurring with different mask sizes
for size in mask_sizes:
    blur_image = cv2.GaussianBlur(image, (size, size), 0)
    cv2.imshow('Blurred {size}x{size}', blur_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
