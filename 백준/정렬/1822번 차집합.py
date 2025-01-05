a,b=map(int,input().split())

a_list=list(map(int,input().split()))
b_list=list(map(int,input().split()))

a_list=set(a_list)
b_list=set(b_list)

result=a_list-b_list
sorted_dict = sorted(result)

if len(sorted_dict)>0:
    print(len(sorted_dict))
    for i in sorted_dict:
        print(i,end=' ')
else:
    print(0)