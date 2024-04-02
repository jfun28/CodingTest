#1. 모험가 길드
n=int(input())
n_list=list(map(int,input().split()))

n_list.sort()
result=0
count=0
for num in n_list:
    count+=1
    if count >=num:
        result+=1
        count=0

print(result)





