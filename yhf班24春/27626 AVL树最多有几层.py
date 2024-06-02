# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 16:52:49 2024

@author: ghp
"""

from functools import lru_cache
@lru_cache
def f(h):
    if h==0:
        return 0
    if h==1:
        return 1
    return f(h-1)+f(h-2)+1
def g(l):
    ans=0
    while f(ans)<=l:
        ans+=1
    return ans
l=int(input())
print(g(l)-1)