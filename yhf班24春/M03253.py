# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 18:48:50 2024

@author: ghp
"""

while True:
    n,p,m=map(int,input().split())
    if (n,p,m)==(0,0,0):
        break
    check=[1]*(n+1)
    ans=[]
    k=p
    i=1
    while len(ans)<n:
       i+=1
       k+=1
       if k>n:
           k-=n
       while check[k]==0:
           k+=1
           if k>n:
               k-=n
       
       if i==m:
           ans.append(k)
           if len(ans)==n:
               break
           check[k]=0
           i=1
           while check[k]==0:
               k+=1
               if k>n:
                   k-=n
    print(','.join(map(str,ans)))
    
    
