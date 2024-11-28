
n=int(input())
meet=[]
count=0

for _ in range(n):
    x,y=map(int,input().split())
    meet.append((x,y))

meet.sort(key=lambda x:(x[1],x[0]))
previous_end = 0
for start, end in meet:
    if start >= previous_end:
        count += 1
        previous_end = end

print(count)


# 우선은 meet를 끝시간을 기준으로 가장 빠른것 부터 정렬해야 한다.
# 처음에 그냥 순서대로 뽑다가 런타임 오류가 생겼다.