# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:10:55 2024

@author: ghp
"""

m,n=map(int,input().split())
a=[list(map(int,input().split())) for i in range(m)]
def maxs(a):
    rows=len(a)
    cols=len(a[0])
    h=[0 for i in range(cols+1)]
    ans=0
 
    for i in range(rows):
        stack=[-1]
        for j in range(cols+1):
            if j==cols or a[i][j]==1:
                x=0
            else:
                x=h[j]+1
            h[j]=x
            while len(stack)>1 and h[stack[-1]]>x:
                ans=max(ans,h[stack[-1]]*(j-stack[-2]-1))
               
                stack.pop()
            stack.append(j)
    return ans
    
print(maxs(a))
                
        