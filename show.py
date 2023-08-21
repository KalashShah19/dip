#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 17:13:51 2023

@author: bmiit202006100110040
"""

import cv2

img = cv2.imread("temp.jpg")

img = cv2.resize(img, (500,500))

cv2.imshow("IMG", img)

cv2.waitKey(0)

cv2.destroyAllWindows()

#0,367   0,405