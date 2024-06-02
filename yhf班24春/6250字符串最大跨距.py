# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 09:00:33 2024

@author: ghp
"""

s,s1,s2=input().split(',')
n=len(s)
m=len(s2)
left=right=-1
for i in range(n):
    if s[i]==s1[0]:
        flag=True
        j=0
        k=i
        while j<len(s1) and k<n:
            if s1[j]!=s[k]:
                flag=False
                break
            j+=1
            k+=1
        if flag:
            left=k-1
            break
for x in range(n-1,-1,-1):
    if s[x]==s2[-1]:
        flag=True
        y=m-1
        z=x
        while y>=0 and z>=0:
            if s2[y]!=s[z]:
                flag=False
                break
            y-=1
            z-=1
        if flag:
            right=z+1
            break
if left==-1 or right==-1 or left>=right:
    print(-1)
else:
    print(right-left-1)
    
            
                
            
            