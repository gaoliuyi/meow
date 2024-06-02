# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 19:41:59 2024

@author: ghp
"""

s=input()
h1=0
h=0
for x in s:
    if x=="d":
        h+=1
        h1=max(h,h1)
    elif x=="u":
        h-=1
h2=0
i=0
def dfs(d):
    global i,h2
    h2=max(h2,d)
    cnt=0
    while i<len(s):
        if s[i]=='d':
            cnt+=1
            i+=1
            dfs(cnt+d)
        else:
            i+=1
            return
dfs(0)
print(f"{h1} => {h2}")
        
    