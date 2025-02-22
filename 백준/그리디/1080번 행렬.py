n,m=map(int,input().split())



graph_original=[]
graph_trans=[]

for _ in range(n):
    graph_original.append(list(map(int,input())))

for _ in range(n):
    graph_trans.append(list(map(int,input())))



def convert_matrix(i,j):
    for y in range(j,j+3):
        for x in range(i,i+3):
            graph_original[y][x]=1-graph_original[y][x]

count=0

for y in range(n - 2):
    for x in range(m - 2):
        if graph_original[y][x] != graph_trans[y][x]: # 일치하지 않는 부분 발생
            convert_matrix(x, y)	# 여기서도 순서 바꿔서 유지 하면서 호출해야한다.		 # 뒤집고
            count += 1		


flag=0
    

for y in range(n):
    for x in range(m):
        if graph_original[y][x] != graph_trans[y][x]:
            flag=1
            
if flag==1:
    print(-1)

else:
    print(count)



