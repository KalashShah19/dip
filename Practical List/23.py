#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:30:44 2023

@author: bmiit202006100110040
"""

import cv2
import pytesseract

# Load the image
image1 = cv2.imread('letter_image1.png')
image2 = cv2.imread('letter_image2.png')
image3 = cv2.imread('letter_image3.png')

# Perform OCR to extract text from the images
text1 = pytesseract.image_to_string(image1)
text2 = pytesseract.image_to_string(image2)
text3 = pytesseract.image_to_string(image3)

# Display the identified text
print("Identified text in image 1:", text1)
print("Identified text in image 2:", text2)
print("Identified text in image 3:", text3)
