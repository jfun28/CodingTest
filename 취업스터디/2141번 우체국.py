import sys
input=sys.stdin.readline

n=int(input())
people=0
village=[]

for _ in range(n):
    pos, peo = map(int, input().split())
    village.append((pos, peo))
    people += peo

village.sort() # 위치가 항상 순서대로 입력된다는 보장은 없다


print(village)