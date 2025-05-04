# '''
# 손님이 먹을 수 있는 초밥의 가짓수의 최대값
# '''
import sys
input=sys.stdin.readline
n,d,k,c=map(int,input().split())

# 레일 위의 스시를 나타내는 리스트
sushi=[]

for _ in range(n):
    sushi.append(int(input()))
    
# d 종류의 스시에 대해서 선택한 연속된 k에 포함된 개수 
check_dish=[0 for _ in range(d+1)]


# 처음부터 k개의 접시를 고른 경우
count=0
for i in range(k): # 만약 이번에 추가된 접시가 이전에 고른 스시가 아닌경우 개수 추가
    if check_dish[sushi[i]]==0:
        count+=1
    check_dish[sushi[i]]+=1
    
    # count의 최대값이 저장될 변수 
    # 쿠폰 스시 포함 여부에 따라 개수를 추가하여 초기화 
    if check_dish[c]==0:
        answer=count+1
        
    else:
        answer=count

# 초기 상태에서 다음 접시를 추가하고 첫 접실을 제거 
# 0~k-1번까지 k개 고른 뒤 k번 째 접시를 넣고, 0번째 접시를 제거 
for i in range(k,n+k-1):
    # 만약 이번에 추가된 접시가 이전에 고른 스시가 아닌경우 개수 추가 
    if check_dish[sushi[i%n]]==0:
        count+=1
    check_dish[sushi[i%n]]+=1
    
    # 이번에 빠진 스시가 1개만 있었으면 개수 빼기=> 슬라이딩으로 맨 왼쪽에 있는 거는 빼줘야한다.  
    if check_dish[sushi[i-k]]==1:
        count-=1
        
    check_dish[sushi[i-k]]-=1
    
    # 쿠폰으로 받는 스시가 지금 고른 접시중에 포함 안되어 있으면 
    # count +1개와 answer를 비교해서 갱신
    
    if check_dish[c]==0:
        answer=max(answer,count+1)
    
    # 아니면 그냥 갱신    
    else:
        answer=max(answer,count)

# count 최댓값 출력
print(answer)













# # dictionary 이용해서 푸는 방법
# import sys
# from collections import defaultdict
# input=sys.stdin.readline

# n,d,k,c=map(int,input().split())

# food_list=[int(sys.stdin.readline()) for _ in range(n)]
    
# food_list.extend(food_list) # 원형이라서 2개를 이어준다.
# left=0
# right=0
# dict_=defaultdict(int)
# result=0


# dict_[c]+=1  #보너스는 무조건 막기


# # 1. 처음에 k 구간만큼 먹기
# while right <k:
#     dict_[food_list[right]]+=1
#     right+=1
    
# # 2. 슬라이딩 윈도우 적용
# while right < len(food_list):
#     result=max(result,len(dict_))
    
#     # 1. 맨 왼쪽 초밥 제거
#     dict_[food_list[left]]-=1
#     if dict_[food_list[left]]==0: # 삭제된 왼쪽 초밥이 0이면 dict 삭제
#         del dict_[food_list[left]]
        
#     # 2.오른쪽 초밥 추가하기
#     dict_[food_list[right]]+=1
    
#     # 왼쪽 위치 +1
#     left+=1
    
#     # 오른쪽 위치 +1
#     right+=1
    

# print(result)
        
    
    
