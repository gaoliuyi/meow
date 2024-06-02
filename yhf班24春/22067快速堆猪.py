# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:27:34 2024

@author: ghp
"""
stack=[]
fstack=[]
while True:
    try:
        s=input()
        if s=="min":
            if fstack:
                print(fstack[-1])
                
        elif s=="pop":
            if stack:
                a=stack.pop()
                if a==fstack[-1]:
                    fstack.pop()
        else:
            a,b=s.split()
            b=int(b)
            stack.append(b)
            if fstack:
                if b<=fstack[-1]:
                    fstack.append(b)
            else:
                fstack.append(b)
    except EOFError:
        break
            
            
        