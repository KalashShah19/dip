#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 18:22:48 2023

@author: bmiit202006100110040
"""
import cv2
import os

def adjecent():
    
    if (main2 < 127):
        if(main2 in {n1,n2,n3,n4}):
            return "4 Adjecent"
        if(main2 in {n5,n6,n7,n8}):
            return "8 Adjecent"
    else:
        return "Not Adjecent"
# =============================================================================
#     else:
#         if(main2 in {n5,n6,n7,n8}):
#             if(n21 not in {n1, n2, n3, n4}):
#                 if(n22 not in {n1, n2, n3, n4}):
#                     if(n23 not in {n1, n2, n3, n4}):
#                         if(n24 not in {n1, n2, n3, n4}):
#                             return "m Adjecent"
# =============================================================================
            
img = cv2.imread("colors.jpg",0)

x = int(input('Enter X coordinate of Pixel 1 : '))
y = int(input('Enter Y coordinate of Pixel 1 : '))

x2 = int(input('Enter X coordinate of Pixel 2 : '))
y2 = int(input('Enter Y coordinate of Pixel 2 : '))

# x=50
# y=50

# x2=51
# y2=59

main = img[x][y]
main2 = img[x2][y2]

n1 = img[x][y-1]
n2 = img[x+1][y]
n3 = img[x][y+1]
n4 = img[x-1][y]

n21 = img[x2][y2-1]
n22 = img[x2+1][y2]
n23 = img[x2][y2+1]
n24 = img[x2-1][y2]

n5 = img[x-1][y-1]
n6 = img[x+1][y-1]
n7 = img[x+1][y+1]
n8 = img[x-1][y]

flag=adjecent() 

cv2.imshow("Pixel 1 = " + str(img[x][y]) + " Pixel 2 = " + str(img[x2][y2]) , img) 

os.system("clear")
           
print(flag)
print("Pixel 1 = " + str(img[x][y]) + " and Pixel 2 = " + str(img[x2][y2])) 

cv2.waitKey(0)
cv2.destroyAllWindows()