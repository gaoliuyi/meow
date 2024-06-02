# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 19:12:38 2024

@author: ghp
"""

n=int(input())
time=[]
a=list(map(int,input().split()))
for i in range(n):
    time.append([i+1,a[i]])
time.sort(key=lambda x:x[1])
ans=0
for i in range(n):
    ans+=(n-i-1)*time[i][1]
    print(time[i][0],end=' ')
print()
ans=ans/n
print("{:.2f}".format(ans))