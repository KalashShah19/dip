#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 17:33:37 2023

@author: bmiit202006100110040
"""

# importing libraries
import cv2
import numpy as n
from matplotlib import pyplot as plt

# reading the input image
img = cv2.imread('temp.jpg')

# define colors to plot the histograms
colors = ('b','g','r')

# compute and plot the image histograms
for i,color in enumerate(colors):
	hist = cv2.calcHist([img],[i],None,[256],[0,256])
	plt.plot(hist,color = color)
plt.title('Image Histogram GFG')
plt.show()

br = int(n.mean(img))
co = int(n.std(img))
mini = min(img)
maxi = max(img)

print()
print("Brightness = " + str(br) + " and Contrast = " + str(co))
print("Min = " + str(mini) + " and Max = " + str(maxi))
