
n=int(input())

meet=[]
count=0

for _ in range(n):
    x,y=map(int,input().split())
    meet.append((x,y))

# meet=sorted(meet,key=lambda x:x[1])
meet.sort(key=lambda x:(x[1],x[0])) # 이렇게 하는 방식이 첫번째로 종료 시간(x[1])을 기준으로 정렬하고 종료 시간이 같은 경우, 시작 시간(x[0])을 기준으로 추가 정렬합니다. 

previous_end=0

for start, end in meet:
    if previous_end<=start:
        count+=1
        previous_end=end

print(count)