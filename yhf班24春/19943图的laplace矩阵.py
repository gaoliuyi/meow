# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:25:03 2024

@author: ghp
"""

class Vertex:
    def __init__(self,key):
        self.id=key
        self.to={}
    def add(self,num,w=0):
        self.to[num]=w
    def __str__(self):
        return str(self.id)+'connected To: '+str([x.id for x in self.to])
    def getto(self):
        return self.to.keys()
    def getid(self):
        return self.id
    def getweight(self,num):
        return self.to[num]
class Graph:
    def __init__(self):
        self.vertlist={}
        self.numvertice=0
    def addvertex(self,key):
        self.numvertice+=1
        newvertex=Vertex(key)
        self.vertlist[key]=newvertex
        return newvertex
    def getvertex(self,n):
        if n in self.vertlist:
            return self.vertlist[n]
        else:
            return None
    def __contains__(self,n):
        return n in self.vertlist
    def addEdge(self, f, t, weight=0):
        if f not in self.vertlist:
            nv = self.addvertex(f)
        if t not in self.vertlist:
            nv = self.addvertex(t)
        self.vertlist[f].add(self.vertlist[t], weight)
    def getVertices(self):
        return self.vertlist.keys()

    def __iter__(self):
        return iter(self.vertlist.values())
def Laplace(n,edges):
    graph=Graph()
    for i in range(n):
        graph.addvertex(i)
    for edge in edges:
        a,b=edge
        graph.addEdge(a,b)
        graph.addEdge(b,a)
    laplace=[]
    for vertex in graph:
        row=[0]*n
        row[vertex.getid()]=len(vertex.getto())
        for nei in vertex.getto():
            row[nei.getid()]=-1
        laplace.append(row)
    return laplace
n,m=map(int,input().split())
edges=[]
for i in range(m):
    a,b=map(int,input().split())
    edges.append((a,b))
laplace=Laplace(n,edges)
for row in laplace:
    print(' '.join(map(str,row)))