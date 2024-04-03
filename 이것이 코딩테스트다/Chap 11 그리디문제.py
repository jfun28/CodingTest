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
# 동시 당발적으로 전부 0으로 바꿀때랑 전부 1로 바꿀때로 count 해줘야한다. 

data=input()
count0=0 # 전부 0으로 바꾸는 경우
count1=0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리

if data[0]=='1':
    count0+=1
else:
    count1+=1

for i in range(len(data)-1):
    if data[i]!=data[i+1]:
        if data[i+1]=='1':
            count0+=1
        else:
            count1+=1

print(min(count0,count1))