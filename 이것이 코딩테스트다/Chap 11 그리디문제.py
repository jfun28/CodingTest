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



# 3번 문자열 뒤집기

n=int(input())
