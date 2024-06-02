# -*- coding: utf-8 -*-
"""
Created on Thu May  2 20:17:19 2024

@author: ghp
"""
ans=[]
def dfs(x,p):
    for i in "12345678":
        if i not in p:
            for j in range(len(p)):
                if abs(int(i)-int(p[j]))==abs(x-j):
                    break
            else:
                if x==7:
                    ans.append(p+i)
                else:
                    dfs(x+1,p+i)
p=''
dfs(0,'')
for _ in range(int(input())):
    print(ans[(int(input()))-1])
    