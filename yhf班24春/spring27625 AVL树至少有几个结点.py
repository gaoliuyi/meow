# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:49:52 2024

@author: ghp
"""

from functools import lru_cache
@ lru_cache(maxsize=None)
def f(n):
    if n==1:
        return 1
    if n==2:
        return 2
    else:
        return f(n-1)+f(n-2)+1
print(f(int(input())))
        