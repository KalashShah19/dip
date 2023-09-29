#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:01:35 2023

@author: bmiit202006100110040
"""

import cv2
import numpy as np

img = cv2.imread("gigs.png",0)
#img = cv2.imread("cam.jpg",0)

cv2.imshow("Original", img)

thresh, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #binary
binary = cv2.bitwise_not(binary)  #complement

cv2.imshow("Binary", binary)

# Creating kernel
struc = np.array([[0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]], np.uint8)

#kernel = np.ones((3,3),np.unit8)

# Using cv2.erode() method
new = cv2.erode(binary, struc)

# Displaying the image
cv2.imshow("erroded", new)

cv2.waitKey(0)

cv2.destroyAllWindows()

# =============================================================================
# cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
# array([[0, 0, 1, 0, 0],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [0, 0, 1, 0, 0]], dtype=uint8)
# =============================================================================
