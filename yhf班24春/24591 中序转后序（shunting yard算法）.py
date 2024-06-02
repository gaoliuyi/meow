# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:30:38 2024

@author: ghp
"""

def trans(s):
    op={'+':1,'-':1,'*':2,"/":2}
    stack=[]
    output=[]
    num=''
    for x in s:
        if x.isnumeric() or x=='.':
            num+=x
        else:
            if num:
                number=float(num) if '.' in num else int(num)
                output.append(number)
                num=''
            if x=="(":
                stack.append(x)
            elif x==")":
                while stack and stack[-1]!='(':
                    output.append(stack.pop())
                stack.pop()
            elif x in op:
                while stack and stack[-1] in op and op[x]<=op[stack[-1]]:
                        output.append(stack.pop())
                stack.append(x)
    if num:
        number=float(num) if '.' in num else int(num)
        output.append(number)
        num=''
    while stack:
        output.append(stack.pop())
    return output
n=int(input())
for i in range(n):
    s=input()
    output=trans(s)
    print(' '.join(map(str,output)))
            
                
            
            