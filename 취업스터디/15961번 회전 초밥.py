import sys
from collections import defaultdict
input=sys.stdin.readline

n,d,k,c=map(int,input().split())
food_list=[]

for _ in range(n):
    food_list.append(int(input()))

food_list.extend(food_list)

left=0
right=0

dict_=defaultdict(int)
result=0
dict_[c]+=1 # 보너스는 무조건 먹기

#1. 처음에 k 구간만큼 먹기
while right<k:
    dict_[food_list[right]]+=1
    right+=1 # 여기서 +1로 끝나니깐 윈도우보다 긴 상태에서 끝난다

#2. 슬라이딩 윈도우 적용
while right<len(food_list):
    result=max(result,len(dict_))

    # 1. 맨 왼쪽 초밥 제거
    dict_[food_list[left]]-=1
    if dict_[food_list[left]]==0: # 중복되어서 겹칠수도 있으니깐 완전히 사라진 경우에만 dict_에서 뺴준다
        del dict_[food_list[left]]

    # 2.오른쪽 초밥 추가하기
    dict_[food_list[right]]+=1 # 다음 오른쪽으로 이동

    left+=1
    right+=1


print(result)
