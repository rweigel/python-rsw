#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 13:40:06 2019

@author: robertweigel
"""


import math

class NiceScale:
    def __init__(self, minv,maxv):
        self.maxTicks = 8
        self.tickSpacing = 0
        self.lst = 10
        self.niceMin = 0
        self.niceMax = 0
        self.minPoint = minv
        self.maxPoint = maxv
        self.calculate()

    def calculate(self):
        self.lst = self.niceNum(self.maxPoint - self.minPoint, False)
        self.tickSpacing = self.niceNum(self.lst / (self.maxTicks - 1), True)
        self.niceMin = math.floor(self.minPoint / self.tickSpacing) * self.tickSpacing
        self.niceMax = math.ceil(self.maxPoint / self.tickSpacing) * self.tickSpacing

    def niceNum(self, lst, rround):
        self.lst = lst
        exponent = 0 # exponent of range */
        fraction = 0 # fractional part of range */
        niceFraction = 0 # nice, rounded fraction */

        exponent = math.floor(math.log10(self.lst));
        fraction = self.lst / math.pow(10, exponent);

        if (self.lst):
            if (fraction < 1.5):
                niceFraction = 1
            elif (fraction < 3):
                niceFraction = 2
            elif (fraction < 7):
                niceFraction = 5;
            else:
                niceFraction = 10;
        else :
            if (fraction <= 1):
                niceFraction = 1
            elif (fraction <= 2):
                niceFraction = 2
            elif (fraction <= 5):
                niceFraction = 5
            else:
                niceFraction = 10

        return niceFraction * math.pow(10, exponent)

    def setMinMaxPoints(self, minPoint, maxPoint):
          self.minPoint = minPoint
          self.maxPoint = maxPoint
          self.calculate()

    def setMaxTicks(self, maxTicks):
        self.maxTicks = maxTicks;
        self.calculate()

a=NiceScale(13, 33)
print("a.lst ", a.lst)
print("a.maxPoint ", a.maxPoint)
print("a.maxTicks ", a.maxTicks)
print("a.minPoint ", a.minPoint)
print("a.niceMax ", a.niceMax)
print("a.niceMin ", a.niceMin)
print("a.tickSpacing ", a.tickSpacing)
print((a.niceMax-a.niceMin)/a.tickSpacing)