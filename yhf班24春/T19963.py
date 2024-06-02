# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 19:20:03 2024

@author: ghp
"""
n=int(input())
pairs = [i[1:-1] for i in input().split()]
dis = [ sum(map(int,i.split(','))) for i in pairs]
p=list(map(int,input().split()))
d=[]
for i in range(n):
    d.append(dis[i]/p[i])
dis1=sorted(d)
p1=sorted(p)
if n%2:
    d2=dis1[n//2]
    p2=p1[n//2]
else:
    d2=(dis1[n//2-1]+dis1[n//2])/2
    p2=(p1[n//2-1]+p1[n//2])/2
ans=0
for i in range(n):
    if d[i]>d2 and p[i]<p2:
        ans+=1
print(ans)

    