n,k=map(int,input().split())
a_list=list(map(int,input().split()))
b_list=list(map(int,input().split()))


a_list.sort()
b_list.sort(reverse=True)


for i in range(k):
    if a_list[i]<b_list[i]:
        a_list[i],b_list[i]=b_list[i],a_list[i]

print(sum(a_list))