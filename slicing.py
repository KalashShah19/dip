#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 17:11:19 2023

@author: bmiit202006100110040
"""

import cv2

img = cv2.imread("1.jpg",0)

mask = cv2.inRange(img, 100,200)

new = cv2.bitwise_and(img, mask, mask)

cv2.imshow("New", new)
cv2.imwrite("slice.jpg", new)

cv2.waitKey(0)

cv2.destroyAllWindows()