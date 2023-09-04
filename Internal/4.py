#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 18:07:51 2023

@author: bmiit202006100110040
"""

import cv2
import numpy as n

img = cv2.imread("4.jpg")

mini = n.min(img)
maxi = n.max(img)

new = ((img - mini) * (255 / (maxi- mini))).astype(n.uint8)

cv2.imshow("New", new)
cv2.imwrite("New4.jpg", new)
cv2.waitKey(0)
cv2.destroyAllWindows()