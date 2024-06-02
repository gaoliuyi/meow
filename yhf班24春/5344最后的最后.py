# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 21:59:38 2024

@author: ghp
"""

n,k=map(int,input().split())
check=[1]*n
ans=[]
x=0
i=0
j=0
while x<n-1:
    i+=1
    if i>n:
        i-=n
    if check[i-1]:
        j+=1
    if j==k:
        check[i-1]=0
        j=0
        ans.append(i)
        x+=1
    
print(*ans)

        
            