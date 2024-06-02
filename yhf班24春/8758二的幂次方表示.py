# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:57:44 2024

@author: ghp
"""

def findans(x):
    def findp(x):
        if x==0:
            return ""
        p=0
        while (1<<p)<=x:
            p+=1
        return p-1
    def giveans(t):
        if t==0:
            return '2(0)'
        elif t==1:
            return '2'
        else:
            return '2('+findans(t)+")"
    ans=''
    while x>0:
        p=findp(x)
        if ans:
            ans+='+'
        ans+=giveans(p)
        x-=1<<p
    return ans
n=int(input())
ans=findans(n)
print(ans)
        