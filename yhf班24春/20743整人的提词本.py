# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 22:27:48 2024

@author: ghp
"""

def reverseword(s):
    stack=[]
    for char in s:
        if char==")":
            temp=[]
            while stack and stack[-1]!="(":
                temp.append(stack.pop())
            if stack:
                stack.pop()
            stack.extend(temp)
        else:
            stack.append(char)
    return "".join(stack)
s=input()
print(reverseword(s))