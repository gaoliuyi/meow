# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 11:43:04 2024

@author: ghp
"""
from collections import deque
s=input()
stack=[]
st=deque()
for x in s:
    if x==")":
        while stack[-1]!="(":
            st.append(stack.pop())
        stack.pop()
        while st:
            stack.append(st.popleft())
    else:
        stack.append(x)
print("".join(stack))
    
    
            
    
    