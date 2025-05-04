'''
손님이 먹을 수 있는 초밥의 가짓수의 최대값
'''
import sys
from collections import defaultdict
input=sys.stdin.readline

n,d,k,c=map(int,input().split())

food_list=[int(sys.stdin.readline()) for _ in range(n)]
    
food_list.extend(food_list) # 원형이라서 2개를 이어준다.
left=0
right=0
dict_=defaultdict(int)
result=0


dict_[c]+=1  #보너스는 무조건 막기

# print("dict_",dict_)

# 1. 처음에 k 구간만큼 먹기
while right <k:
    dict_[food_list[right]]+=1
    right+=1
    
# 2. 슬라이딩 윈도우 적용
while right < len(food_list):
    result=max(result,len(dict_))
    
    # 1. 맨 왼쪽 초밥 제거
    dict_[food_list[left]]-=1
    if dict_[food_list[left]]==0: # 삭제된 왼쪽 초밥이 0이면 dict 삭제
        del dict_[food_list[left]]
        
    # 2.오른쪽 초밥 추가하기
    dict_[food_list[right]]+=1
    
    # 왼쪽 위치 +1
    left+=1
    
    # 오른쪽 위치 +1
    right+=1
    
# print("answer_dict_",dict_)    
    
print(result)
        
    
    
