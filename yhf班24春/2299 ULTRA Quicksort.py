# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 20:46:01 2024

@author: ghp
"""
def mergesort(arr,temp,left,right):
    if right-left<=1:
        return 0
    mid=(left+right)//2
    num=mergesort(arr,temp,left,mid)+mergesort(arr,temp,mid,right)
    i,j,k=left,mid,left
    while i<mid and j<right:
        if arr[i]<arr[j]:
            temp[k]=arr[i]
            i+=1
        else:
            temp[k]=arr[j]
            num+=mid-i
            j+=1
        k+=1
    while i<mid:
        temp[k]=arr[i]
        i+=1
        k+=1
    while j<right:
        temp[k]=arr[j]
        j+=1
        k+=1
    for i in range(left,right):
        arr[i]=temp[i]
    return num
while True:
    n=int(input())
    if n==0:
        break
    p=[]
    for i in range(n):
        p.append(int(input()))
    temp=[0]*n
    ans=mergesort(p,temp,0,n)
    print(ans)
        