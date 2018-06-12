#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 21:02:43 2018

@author: drjayantisinha
"""

x = 27
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (low + high) / 2.0
while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans), 'is close to square root of ' + str(x))
