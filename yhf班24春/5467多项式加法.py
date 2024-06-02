# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 10:21:02 2024

@author: ghp
"""

n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    d={}
    for j in range(1,len(a)-2,2):
        if a[j] in d:
            d[a[j]]+=a[j-1]
        else:
            d[a[j]]=a[j-1]
    for j in range(1,len(b)-2,2):
        if b[j] in d:
            d[b[j]]+=b[j-1]
        else:
            d[b[j]]=b[j-1]
    
    e=list(d.keys())
    e.sort(reverse=True)
    for k in range(len(e)):
        if d[e[k]]!=0:
            print('[ {} {} ]'.format(d[e[k]],e[k]),end=' ')
    print()
        
            
            
        
    
    
    
    