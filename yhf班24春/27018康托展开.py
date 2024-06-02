# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:14:02 2024

@author: ghp
"""

n,mod,ans=int(input()),998244353,1
a,fac=list(map(int,input().split())),[1]
tree=[0]*(n+1)
def lowbit(x):
    return x&-x
def update(x,y):
    while x<=n:
        tree[x]+=y
        x+=lowbit(x)
def getsum(x):
    tot=0
    while x:
        tot+=tree[x]
        x-=lowbit(x)
    return tot
for i in range(1,n):
    fac.append(fac[i-1]*i%mod)
for i in range(1,n+1):
    cnt=getsum(a[i-1])
    update(a[i-1],1)
    ans=(ans+((a[i-1]-1-cnt)*fac[n-i])%mod)%mod
print(ans)