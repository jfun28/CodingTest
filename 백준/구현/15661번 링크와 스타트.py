import sys
from itertools import combinations
n=int(input())
graph=[]
input=sys.stdin.readline

for _ in range(n):
    graph.append(list(map(int,input().split())))

# 스타트팀 능력치 구하는 함수

def start_team():
    for 