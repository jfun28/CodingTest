'''
1. 한번 뒤로 가서 점검해볼 것
'''

n=19
graph=[]
whites=[]
blacks=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            blacks.append((i,j))

        elif graph[i][j]==2:
            whites.append((i,j))
        

def search(omoks):
    dx=[1,0,1,-1]
    dy=[1,1,0,1]

    for r,c in omoks:
        for i in range(4):
            cnt=0
            for k in range(1,6):
                nr=r+dx[i]*k
                nc=c+dy[i]*k

                if nr<0 or nr>=n or nc<0 or nc>=n:
                    continue

                if (nr,nc) not in omoks:
                    break

                if (nr,nc) in omoks:
                    cnt+=1

            tr=r-dx[i]
            tc=c-dy[i]

            if (tr,tc) not in omoks and cnt==4:
                return (r+1,c+1)
    
    return False


white_search=search(whites)
black_search=search(blacks)

if white_search:
    print(2)
    print(*white_search)

elif black_search:
    print(1)
    print(*black_search)

