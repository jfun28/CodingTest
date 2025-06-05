from itertools import combinations

n=1
t_n_list=[]
while n!=0:
    n_list=list(map(int,input().split()))
    n=n_list[0]
    if n!=0:
        t_n_list.append(n_list[1:])


for index_num,i_t_n_list in enumerate(t_n_list):
    for i in combinations(i_t_n_list,6):
        print(*i)
    if index_num!=len(t_n_list)-1:
        print()

