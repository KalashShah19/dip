#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:24:22 2023

@author: bmiit202006100110040
"""

import cv2
import numpy as np

room = cv2.imread('temp.png')
logo = cv2.imread('pt.jpg')

#--- Resizing the logo to the shape of room image ---
logo = cv2.resize(logo, (room.shape[1], room.shape[0]))

#--- Apply Otsu threshold to blue channel of the logo image ---
ret, logo_mask = cv2.threshold(logo[:,:,0], 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
cv2.imshow('logo_mask', logo_mask)

room2 = room.copy() 

#--- Copy pixel values of logo image to room image wherever the mask is white ---
room2[np.where(logo_mask == 255)] = logo[np.where(logo_mask == 255)]

cv2.imshow('result.jpg', room2)
cv2.waitKey(0)
cv2.destroyAllWindows()