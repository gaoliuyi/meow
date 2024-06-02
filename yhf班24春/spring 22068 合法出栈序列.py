# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:39:23 2024

@author: ghp
"""

x=input()
while True:
    try:
        s=input()
        if len(s)!=len(x):
            print('NO')
        else:
            stack=[]
            i=0
            for y in x:
                if y!=s[i]:
                    stack.append(y)
                else:
                    i+=1
                    while stack and stack[-1]==s[i]:
                        stack.pop()
                        i+=1
            if i==len(x):
                print('YES')
            else:
                print('NO')
    except EOFError:
        break
                    