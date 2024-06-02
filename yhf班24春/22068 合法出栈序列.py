# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:19:51 2024

@author: ghp
"""

s=input()
def check(x):
    if len(x)!=len(s):
        return 'NO'
    p=0
    q=0
    stack=[]
    while q<len(s):
        if stack and stack[-1]==x[q]:
            stack.pop()
            q+=1
        elif p<len(s):
            stack.append(s[p])
            p+=1
        else:
            return 'NO'
    return 'YES'
while True:
    try:
        print(check(input()))
    except EOFError:
        break            
            
    