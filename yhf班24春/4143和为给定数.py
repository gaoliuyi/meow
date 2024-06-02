# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 20:42:37 2024

@author: ghp
"""

n=int(input())
num=list(map(int,input().split()))
m=int(input())
num.sort()
l=0
r=n-1
flag=0
while l<r:
    if num[l]+num[r]==m:
        print(num[l],num[r])
        flag=1
        break
    elif num[l]+num[r]<m:
        l+=1
    else:
        r-=1
if flag==0:
    print('No')