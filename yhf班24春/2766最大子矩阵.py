# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 15:44:14 2024

@author: ghp
"""

def max_submatrix(matrix):
    def kadane(arr):
        max_end_here=max_so_far=arr[0]
        for x in arr[1:]:
            max_end_here=max(x,x+max_end_here)
            max_so_far=max(max_end_here,max_so_far)
        return max_so_far
    rows=len(matrix)
    cols=len(matrix[0])
    max_sum=float('-inf')
    
    for left in range(cols):
        temp=[0]*rows
        for right in range(left,cols):
            for row in range(rows):
                temp[row]+=matrix[row][right]
            max_sum=max(max_sum,kadane(temp))
    return max_sum
n=int(input())
nums=[]
while len(nums)<n*n:
    nums.extend(input().split())
matrix=[list(map(int,nums[i*n:n*(i+1)])) for i in range(n)]
print(max_submatrix(matrix))
    