# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 21:25:41 2024

@author: ghp
"""
from math import log2
while True:
    try:
        y=int(input())
        left=y**(1/2)-1
        right=y**(1/2)
        while right-left>=0.00001:
            mid=(left+right)/2
            num=mid**2+mid+1+log2(mid)
            if num<=y:
                left=mid
            else:
                right=mid
        print("{:.4f}".format(left))
    except EOFError:
        break