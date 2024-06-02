# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:07:47 2024

@author: ghp
"""

l=input().split("+")
a=0
for i in range(len(l)):
    b,c=l[i].split("^")
    if b!='0n':
        a=max(a,int(c))
print("n^{}".format(a))