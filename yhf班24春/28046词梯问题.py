# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 20:38:33 2024

@author: ghp
"""

from collections import deque,defaultdict
from itertools import permutations
basket=defaultdict(list)
for _ in range(int(input())):
    word=input()
    for i in range(4):
        l=list(word)
        l[i]='-'
        basket["".join(l)].append(word)
graph=defaultdict(list)
for words in basket.values():
    for a,b in permutations(words,2):
        graph[a].append(b)
        graph[b].append(a)
start,end=input().split()
q=deque([start])
path={}
vis=set(q)
def bfs():
    while q:
        now=q.popleft()
        for new in graph[now]:
            if new not in vis:
                vis.add(new)
                path[new]=now
                q.append(new)
            if new==end:
                return True
ans=bfs()
if ans:
    n=end
    p=[n]
    while n in path:
        n=path[n]
        p.append(n)
    p.reverse()
    print(*p)
else:
    print('NO')
        
        
    
    

    
    
