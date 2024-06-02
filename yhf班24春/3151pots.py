# -*- coding: utf-8 -*-
"""
Created on Thu May  2 20:34:18 2024

@author: ghp
"""

from collections import deque
def bfs(A,B,C):
    q=deque()
    q.append((0,0,0,[]))
    v=set()
    v.add((0,0))
    while q:
        a,b,c,d=q.popleft()
        if a==C or b==C:
            return c,d
        for i in range(3):
            if i==0:
                for j in range(2):
                    if j==0 and a!=A:
                        na=A
                        if (na,b) not in v:
                            nd=d[:]
                            nd.append('FILL(1)')
                            q.append((na,b,c+1,nd))
                            v.add((na,b))
        
                        
                    elif j==1 and b!=B:
                        nb=B
                        if (a,nb) not in v:
                            v.add((a,nb))
                            nd=d[:]
                            nd.append('FILL(2)')
                            q.append((a,nb,c+1,nd))
            if i==1:
                for j in range(2):
                    if j==0 and a!=0:
                        na=0
                        if (na,b) not in v:
                            nd=d[:]
                            nd.append('DROP(1)')
                            q.append((na,b,c+1,nd))
                            v.add((na,b))
                    elif j==1 and b!=0:
                        nb=0
                        if (a,nb) not in v:
                            v.add((a,nb))
                            nd=d[:]
                            nd.append('DROP(2)')
                            q.append((a,nb,c+1,nd))
            else:
                for j in range(2):
                    if j==0 and a!=0:
                        nb=min(B,a+b)
                        na=a+b-nb
                        if (na,nb) not in v:
                            nd=d[:]
                            nd.append('POUR(1,2)')
                            q.append((na,nb,c+1,nd))
                            v.add((na,nb))
                    elif j==1 and b!=0:
                        na=min(A,a+b)
                        nb=a+b-na
                        if (na,nb) not in v:
                            nd=d[:]
                            nd.append('POUR(2,1)')
                            q.append((na,nb,c+1,nd))
                            v.add((na,nb))
    return 'impossible',0
x,y,z=map(int,input().split())
t,ans=bfs(x,y,z)
if t=="impossible":
    print(t)
else:
    print(t)
    for k in ans:
        print(k)
                
                        
                    
                
                        
                        