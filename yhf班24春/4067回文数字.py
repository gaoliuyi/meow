# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 19:19:51 2024

@author: ghp
"""

while True:
    try:
        s=list(input())
        a=s[:]
        s.reverse()
        if str(a)==str(s):
            print('YES')
        else:
            print('NO')
    except EOFError:
        break