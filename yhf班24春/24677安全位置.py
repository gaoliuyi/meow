# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:59:33 2024

@author: ghp
"""

parts=[]
def dfs(s,depth=0):
    ans=0
    if depth==4:
        if not s and all (0<=int(part)<=500 and (part=='0' or part[0]!='0') for part in parts) :
            return 1
        return 0
    for i in range(1,len(s)+1):
        parts.append(s[:i])
        x=dfs(s[i:],depth+1)
        ans+=x
        parts.pop()
    return ans
s=input().strip()
print(dfs(s,0))
    