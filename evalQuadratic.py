#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 03:40:18 2018

@author: drjayantisinha
"""

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numberical value at which to evaluate the quadratic
    '''
    return a*(x**2) + b*x + c

print(evalQuadratic(1,1,1,0))