n,m=map(int,input().split())
block=list(map(int,input().split()))
result=0

for i in range(1,m-1): # 맨 왼쪽과 맨 오른쪽은 물이 고일 수 없으니깐 패스
    left_max=max(block[:i])
    right_max=max(block[i+1:])

    lower_criteria=min(left_max,right_max)
    if block[i]<lower_criteria:
        result+=lower_criteria-block[i]

print(result)

    
