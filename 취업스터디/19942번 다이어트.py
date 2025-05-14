import sys
INF = sys.maxsize
input=sys.stdin.readline
n = int(input())
mp,mf,ms,mv = map(int, input().split()) # 단백질, 탄수화물, 지방, 비타민
arr = [list(map(int, input().split())) for _ in range(n)]

temp = []
result = []
cost = INF

def check(array):
    global cost, result
    p,f,s,v,c = 0,0,0,0,0
    for arr in array:
        p += arr[0]
        f += arr[1]
        s += arr[2]
        v += arr[3]
        c += arr[4]

    if p >= mp and f >= mf and s >= ms and v >= mv:
        if c < cost:
            cost = c
            result = [x[5] + 1 for x in temp]
        return True
    else:
        return False

def backtracking(start):
    if check(temp):
        return

    for i in range(start, len(arr)):
        temp.append(arr[i] + [i])
        backtracking(i+1)
        temp.pop()

backtracking(0)

if cost == INF:
    print(-1)
else:
    print(cost)
    print(' '.join(map(str, result)))





# import sys
# input=sys.stdin.readline
# n=int(input())

# mp,mf,ms,mv=map(int,input().split())

# ingredient=[]
# price=[]

# for _ in range(n):
#     ingredient.append(map(int,input().split()))
    


    