def dfs(depth,idx):
    if depth==6:
        print(*out)
        return
    
    for i in range(idx,k):
        out.append(s[i])
        dfs(depth+1,i+1)
        out.pop()




while True:
    array=list(map(int,input().split()))
    k=array[0]
    s=array[1:]

    out=[]
    dfs(0,0)
    if k==0:
        exit()
    print()












# from itertools import combinations

# n=1
# t_n_list=[]
# while n!=0:
#     n_list=list(map(int,input().split()))
#     n=n_list[0]
#     if n!=0:
#         t_n_list.append(n_list[1:])


# for index_num,i_t_n_list in enumerate(t_n_list):
#     for i in combinations(i_t_n_list,6):
#         print(*i)
#     if index_num!=len(t_n_list)-1:
#         print()

