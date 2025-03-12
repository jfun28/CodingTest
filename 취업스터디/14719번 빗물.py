n,m=map(int,input().split())
block=list(map(int,input().split()))
result=0

for i in range(1,m-1): # 맨 왼쪽과 맨 오른쪽은 물이 고일 수 없으니깐 패스
    left_max=max(block[:i]) # 맨 왼쪽에서 가장 큰 블록 
    right_max=max(block[i+1:]) # 오른쪽에서 가장 큰 블록

    lower_criteria=min(left_max,right_max) # 왼쪽, 오른쪽 기준으로 가장 낮은걸 채운다.
    if block[i]<lower_criteria: # 가장 낮은 기둥이 현재 상태 블록보다 높다면 물이 채워진다.
        result+=lower_criteria-block[i] # 그 값 차이만큼 채워지면서 더한다.

print(result)

    
