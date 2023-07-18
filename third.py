#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 16:48:17 2023

@author: bmiit202006100110040
"""

import cv2
import os

img = cv2.imread("colors.jpg")

x = int(input('Enter X coordinate : '))
y = int(input('Enter Y coordinate : '))

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
print()
print("4-neighbors : ")
print()
print("Up Neighbor " + str(n4) + " at (" + str(x-1) + "," + str(y)+")")
print("Left Neighbor = " + str(n1) + " at (" + str(x) + "," + str(y-1)+")")
print("Down Neighbor " + str(n2) + " at (" + str(x+1) + "," + str(y)+")")
print("Right Neighbor " + str(n3) + " at (" + str(x) + "," + str(y+1)+")")
print()
print("8-neighbors : ")
print()
print("Up Left Neighbor " + str(n5) + " at (" + str(x-1) + "," + str(y-1)+")")
print("Up Right Neighbor = " + str(n6) + " at (" + str(x+1) + "," + str(y-1)+")")
print("Down Right Neighbor " + str(n8) + " at (" + str(x+1) + "," + str(y+1)+")")
print("Down Left Neighbor " + str(n7) + " at (" + str(x-1) + "," + str(y+1)+")")

cv2.waitKey(0)
cv2.destroyAllWindows()