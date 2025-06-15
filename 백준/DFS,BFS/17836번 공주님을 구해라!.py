import sys
input=sys.stdin.readline

n,m,T=map(int,input().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))


visited=[]

def dfs(v):
    