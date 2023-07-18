#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 18:22:48 2023

@author: bmiit202006100110040
"""
import cv2
import os

img = cv2.imread("colors.jpg",0)

# =============================================================================
# x = int(input('Enter X coordinate : '))
# y = int(input('Enter Y coordinate : '))
# =============================================================================

x=50
y=50

x2=51
y2=51

main = img[x][y]
n1 = img[x][y-1]
n2 = img[x+1][y]
n3 = img[x][y+1]
n4 = img[x-1][y]

n5 = img[x-1][y-1]
n6 = img[x+1][y-1]
n7 = img[x+1][y+1]
n8 = img[x-1][y]

cv2.imshow("Pixel Value = " + str(img[x][y]), img)



os.system("clear")

print("Pixel = " + str(main) + " at " + str(x) + "," + str(y))

cv2.waitKey(0)
cv2.destroyAllWindows()