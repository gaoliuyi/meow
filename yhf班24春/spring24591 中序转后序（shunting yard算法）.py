# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:29:01 2024

@author: ghp
"""

def shuntingyard(s):
    stack=[]
    ans=[]
    num=''
    p={"+":1,"-":1,"*":2,"/":2}
    for x in s:
    
        if x.isnumeric() or x=='.':
            num+=x
        else:
            if num:
                ans.append(num)
                num=''
            if x=="(":
                stack.append(x)
            elif x==")":
                while stack and stack[-1]!='(':
                    ans.append(stack.pop())
                stack.pop()
            elif x in p:
                while stack and stack[-1] in p and p[stack[-1]]>=p[x]:
                    ans.append(stack.pop())
                stack.append(x)
        
    if num:
        ans.append(num)
        num=''
    while stack:
       
        ans.append(stack.pop())
        
    return ans
for i in range(int(input())):
    s=input()
    ans=shuntingyard(s)
    print(*ans)
                    
    