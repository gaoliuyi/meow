# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 09:14:17 2024

@author: ghp
"""
st=[]
stack=[]
while True:
    try:
        s=input()
        if s=='min':
            if st:
                print(st[-1])
        elif s=="pop":
            if stack:
                a=stack.pop()
                if a==st[-1]:
                    st.pop()
            
        else:
            b,c=s.split()
            c=int(c)
            stack.append(c)
            if st:
                if st[-1]>=c:
                    st.append(c)
                    
            else:
                st.append(c)
    except EOFError:
        break