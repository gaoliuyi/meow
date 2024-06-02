# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 20:57:09 2024

@author: ghp
"""

a,b,c,d=map(int,input().split())
i=1
while True:
    if b*i%d==0:
        break
    else:
        i+=1
x=b*i//d
y=a*i+c*x
z=b*i
def prime(y,z):
    if y==1 or z==1:
        return 1
    elif y>=z:
        if y%z!=0:
            return prime(y%z,z)
        else:
            return z
    elif y<z:
        if z%y!=0:
            return prime(z%y,y)
        else:
            return y
e=prime(y,z)
ans1=y//e
ans2=z//e
print(f"{ans1}/{ans2}")
        
    