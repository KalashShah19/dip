#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 16:49:46 2023

@author: bmiit202006100110040
"""

import cv2

img = cv2.imread("py.png", 0)
cv2.imshow("original", img)
width, height = img.shape
# print(width, height, dimension)

# img[0][0][0]=255
# img[0][0][1]=255
# img[0][0][2]=255
# img[0][1][0]=255
# img[0][1][1]=255
# img[0][1][2]=255
# img[0][2][0]=255
# img[0][2][1]=255

# Black Strip

# for i in range(0, 855):
#     for j in range(0, 3):
#         for k in range(0, 25):
#             img[k][i][j]=0

# Brighten Pixels 

for i in range(0, width-1):
    for j in range(0, height-1):
        if(img[i][j] <= 150):
            img[i][j]+=50


cv2.imshow("Manipulation", img)

cv2.waitKey(0)

cv2.destroyAllWindows()