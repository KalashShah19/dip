#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 17:18:32 2023

@author: bmiit202006100110040
"""

import cv2
import numpy as n
from matplotlib import pyplot as plt
 
img = cv2.imread("3.jpg",0)

hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist, color='b')
plt.title('Image Histogram For Blue Channel GFG')
plt.show()

cv2.imshow("Original", img)

gamma = 0.4

new = n.array(255*(img / 255) ** gamma, dtype = 'uint8')

cv2.imshow("New", new)
cv2.imwrite("New3.jpg", new)
newHist = cv2.calcHist([new],[0],None,[256],[0,256])
plt.plot(newHist, color='b')
plt.title('Image Histogram For Blue Channel GFG')
plt.show()

cv2.waitKey(0)

cv2.destroyAllWindows()