import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n=int(input)
graph=[]

for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs():