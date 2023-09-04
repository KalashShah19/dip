#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 17:35:25 2023

@author: bmiit202006100110040
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread("5.jpg",0)

hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist, color='b')
plt.show()

cv2.imshow("Original", img)

thresh, new = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary", new)
cv2.imwrite("Binary.jpg", new)

cv2.waitKey(0)

cv2.destroyAllWindows()