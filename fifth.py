#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 18:22:48 2023

@author: bmiit202006100110040
"""

import math
import os

x1 = int(input("Enter Value of X1 : "))
y1 = int(input("Enter Value of y1 : "))
x2 = int(input("Enter Value of X2 : "))
y2 = int(input("Enter Value of y2 : "))

os.system("clear")

de = int(math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)))
print("Answer : ")
print("Distance = " + str(de))
