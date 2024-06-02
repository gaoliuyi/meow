# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:40:42 2024

@author: ghp
"""
from collections import deque
while 1:
    n=int(input())
    if n==0:
        break
    q=deque()
    q.append((1,'1'))
    visited={1}
    while q:
        remain,num=q.popleft()
        if remain==0:
            print(num)
            break
        for i in range(0,2):
            newremain=(remain*10+i)%n
            newnum=num+str(i)
            if newremain not in visited:
                visited.add(newremain)
                q.append((newremain,newnum))
            
        