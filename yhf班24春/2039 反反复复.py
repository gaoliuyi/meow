# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 19:12:01 2024

@author: ghp
"""

n=int(input())
s=input()
a=len(s)//n
mat=[[0]*n for i in range(a)]
y=len(s)
x=0
while x<y:
    for i in range(a):
        if i%2==0:
            for j in range(n):
                mat[i][j]=s[x]
                x+=1
        else:
            for j in range(n-1,-1,-1):
                mat[i][j]=s[x]
                x+=1
ans=''
for j in range(n):
    for i in range(a):
        ans=ans+mat[i][j]
print(ans)
    