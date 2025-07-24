n,k=map(int,input().split())

num_list=list(map(int,input().split()))
count=0
count_list=[]
dict_={}
for num in num_list:
    if num not in dict_:
        dict_[num]=1
    else:
        dict_[num]+=1

    if dict_[num]>k:
        count_list.append(count)
        count=0
        continue
    count+=1

print(max(count_list))



