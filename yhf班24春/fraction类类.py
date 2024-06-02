# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 15:27:35 2024

@author: ghp
"""

import math
class Fraction:
    def __init__(self,up,down):
        self.up=up
        self.down=down
    def __str__(self):
        return str(self.up)+'/'+str(self.down)
    def __add__(self,other):
        newup=self.up*other.down+self.down*other.up
        newdown=self.down*other.down
        n=math.gcd(newup,newdown)
        return Fraction(newup//n,newdown//n)
a,b,c,d=map(int,input().split())
x=Fraction(a,b)
y=Fraction(c,d)
print(x+y)
