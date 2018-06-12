#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 02:27:56 2018

@author: drjayantisinha
"""

s = "hello, world"
num_vowels = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        num_vowels += 1
print(num_vowels)
        