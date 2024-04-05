import time
# #1. 모험가 길드
# n=int(input())
# n_list=list(map(int,input().split()))

# n_list.sort()
# result=0
# count=0
# for num in n_list:
#     count+=1
#     if count >=num:
#         result+=1
#         count=0

# print(result)

# # 2.곱하기 혹은 더하기 

# n=input()
# stack=[]
# n_list=list(n)
# result=0
# for num in range(len(n_list)-1):
#     first=int(n_list.pop(0))
#     two=int(n_list.pop(0))
#     if first==0 or first==1:
#         result=first+two
#         n_list.insert(0,result)
#         continue
#     result=first*two
#     n_list.insert(0,result)

# print(result)



# # 3번 문자열 뒤집기
# # 동시 당발적으로 전부 0으로 바꿀때랑 전부 1로 바꿀때로 count 해줘야한다. 

# data=input()
# count0=0 # 전부 0으로 바꾸는 경우
# count1=0 # 전부 1로 바꾸는 경우

# # 첫 번째 원소에 대해서 처리

# if data[0]=='1':
#     count0+=1
# else:
#     count1+=1

# for i in range(len(data)-1):
#     if data[i]!=data[i+1]:
#         if data[i+1]=='1':
#             count0+=1
#         else:
#             count1+=1

# print(min(count0,count1))

# #4 만들 수 없는 금액

# n=int(input())

# m_list=list(map(int,input().split()))
# m_list.sort()
# target=1
# for i in m_list:
#     if target<i:
#         

#     target+=i 
# print(target)

# 5 볼링공 고르기
# # ################내가 푼 풀이#####################


# n,m=map(int,input().split())
# n_list=list(map(int,input().split()))
# match_num=0
# start = time.perf_counter()
# for index in range(len(n_list)-1):
#     standard=n_list[index]
#     for compare_index in range(index,len(n_list)):
#         if standard!=n_list[compare_index]:
#             match_num+=1
# end = time.perf_counter()

# print(match_num)
# print(f"{end - start:.5f} sec")

# ################# 정답 풀이########################3333

# n,m=map(int,input().split())
# data=list(map(int,input().split()))

# # 1부터 10까지의 무게를 담을 수 있는 리스트
# start = time.perf_counter()

# array=[0]*11

# # 각 무게에 해당하는 볼링공의 개수 카운트
# for x in data:
#     array[x]+=1

# result=0

# #1부터 m까지의 각 무게에 대하여 처리
# for i in range(1,m+1):
#     n-=array[i] #무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외

#     result+=array[i]*n
# end = time.perf_counter()

# print(result)
# print(f"{end - start:.5f} sec")

# 06 무지개 먹방 라이브

import heapq

def solution(food_times,k):
    
    answer=0

    hq=[]

    for i in range(len(food_times)):
        heapq.heappush(hq,(food_times[i],i+1))

    length=len(hq) # 음식 갯수 (한 사이클)
    pre=0 # 전 음식의 섭취 기간

    while hq:
        # 가장 적은 섭취시간과 전 음식시간의 섭취시간을 빼주고, 음식 개수를 곱함
        diff=(hq[0][0]-pre)*length

        #한 사이클의 음식량을 빼줄 diff가 k보다 작거나 같으면 빼준다. 

        if diff<=k:
            k-=diff
            #한사이클을 돌렸기 때문에 해당 음식은 다먹었으니 제외 시킨다. 

            





