# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 21:35:46 2024

@author: ghp
"""

tree=list(input())+['']
h1=0
cnt=0
for i in range(len(tree)):
    if tree[i]=='d':
        cnt+=1
        h1=max(h1,cnt)
    else:
        cnt-=1
h2=0
i=0
def dfs(d2):
    cnt=1
    global i,h2
    h2=max(h2,d2)
    while tree[i]:
        if tree[i]=='d':
            i+=1
            dfs(d2+cnt)
            cnt+=1
        else:
            i+=1
            return
dfs(0)
print(f"{h1} => {h2}")