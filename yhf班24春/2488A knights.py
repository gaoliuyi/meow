# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:24:30 2024

@author: ghp
"""
for k in range(int(input())):
    print(f'Scenario #{k+1}:')
    dire=[(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
    p,q=map(int,input().split())
    vis=[[True]*(p+1) for i in range(q+1)]
    ans=[]
    vis[1][1]=False
    def dfs(x,y,i):
        global ans
       
        if i==p*q:
            return True
        for dx,dy in dire:
            nx=x+dx
            ny=y+dy
           
            if 1<=nx<=q and 1<=ny<=p and vis[nx][ny]:
                vis[nx][ny]=False
                if dfs(nx,ny,i+1):
                    ans.append(chr(nx+64)+str(ny))
                    return True
                vis[nx][ny]=True
        return False
    if dfs(1,1,1):
        ans.append('A1')
        ans.reverse()
        
        print(''.join(ans))
    else:
        print('impossible')
    print()
                
                
    
    
    