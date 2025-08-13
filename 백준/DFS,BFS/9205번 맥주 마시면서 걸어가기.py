# https://www.acmicpc.net/problem/9205

import sys
from collections import deque
input=sys.stdin.readline

T=int(input())



def bfs(q,visited):
    while q:
        for i in range(1,n+2) :
            if visited[i]==False and dis:




for _ in range(T):
    n=int(input())
    home=[int(x) for x in input().split()]
    conv=[]

    for j in range(n):

    visited=[False]*(n+2)

    q=deque((0,0))
    visited[0]=True


    for _ in range(n+2):
        x,y=map(int,input().split())
        distance.append((x,y))

    
    bfs(q,visited)


