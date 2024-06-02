# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:36:51 2024

@author: ghp
"""

class root:
    def __init__(self,name):
        self.name=name
        self.d=[]
        self.f=[]
    def build(self,s):
        if s[0]=='f':
            self.f.append(s)
        if s[0]=='d':
            di=root(s)
            self.d.append(di)
            while True:
                s=input()
                if s==']':
                    break
                di.build(s)
def pout(r,i=0):
    print('|     '*i+r.name)
    if r.d:
        for x in r.d:
            pout(x,i+1)
    r.f.sort()
    for y in r.f:
        print('|     '*i+y)
x=0
while True:
    s=input()
    if s=='#':
        break
    x+=1
    r=root('ROOT')
    while True:
        r.build(s)
        s=input()
        if s=='*':
            break
    print(f'DATA SET {x}:')
    pout(r,0)
    print()
                
                
            
            
        