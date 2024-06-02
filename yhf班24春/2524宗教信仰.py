# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:38:40 2024

@author: ghp
"""
def solve(x,j):
    if ans[x]==0:
        ans[x]=j
    else:
        return
    if x in a:
        for y in a[x]:
            solve(y,j)
i=0
while True:
    i+=1
    n,m=map(int,input().split())
    if (n,m)==(0,0):
        break
    else:
        ans=[0]*(n+1)
        a={}
        for _ in range(m):
            b,c=map(int,input().split())
            if b not in a:
                a[b]=[c]
            else:
                a[b].append(c)
            if c not in a:
                a[c]=[b]
            else:
                a[c].append(b)
    j=0
    for k in range(1,n+1):
        if ans[k]==0:
            j+=1
            x=k
            solve(x,j)
    print(f"Case {i}: {max(ans)}")                    

        