#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 16:46:27 2023

@author: bmiit202006100110040
"""

import cv2
import os

img = cv2.imread("pt.jpg",0)

img = cv2.resize(img, (780, 540),interpolation = cv2.INTER_LINEAR)

last = img[-1][0]

# =============================================================================
# (thresh, img) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# =============================================================================

cv2.imshow("Clean", img)

os.system("clear")

print(last)

cv2.waitKey(0)

cv2.destroyAllWindows()