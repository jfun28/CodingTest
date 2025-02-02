import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

t=int(input())
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]

k=int(input())
room=list(map(int,input().split()))

    
