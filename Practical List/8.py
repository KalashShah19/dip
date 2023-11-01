#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:00:39 2023

@author: bmiit202006100110040
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

def contrast_stretching(image_path, new_min=0, new_max=255):
    # Read the image
    image = cv2.imread("py.jpg")
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.show()

    # Get the current minimum and maximum intensities
    min_intensity = np.min(image)
    max_intensity = np.max(image)

    # Calculate the scaling factors
    scale = (new_max - new_min) / (max_intensity - min_intensity)
    shifted_image = (image - min_intensity) * scale + new_min

    # Ensure pixel values are within the specified range
    contrast_stretched_image = np.clip(shifted_image, new_min, new_max).astype(np.uint8)

    return contrast_stretched_image

if __name__ == "__main__":
    image_path = "py.jpg"
    contrast_stretched_image = contrast_stretching(image_path)
    
    # Display the original and contrast-stretched images
    cv2.imshow("Original Image", cv2.imread(image_path))
    cv2.imshow("Contrast-Stretched Image", contrast_stretched_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
