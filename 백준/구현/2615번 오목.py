import sys
input=sys.stdin.readline
k=19
graph=[]
whites_blank=[]
blacks_blank=[]

for _ in range(k):
    graph.append(list(map(int,input().split())))

for i in range(k):
    for j in range(k):
        if graph[i][j]==1:
            blacks_blank.append((i,j))

        elif graph[i][j]==2:
            whites_blank.append((i,j))


def search(omoks):
    dx=[1,1,0,-1]
    dy=[1,0,1,1]

    for x,y in omoks:
        for i in range(4):
            cnt=0
            for g in range(1,6): # 
                nx=x+dx[i]*g
                ny=y+dy[i]*g

                if nx<0 or nx>=k or ny<0 or ny>=k:
                    continue

                if (nx,ny) not in omoks:
                    break

                if (nx,ny) in omoks:
                    cnt+=1
                   

            tx=x-dx[i]
            ty=y-dy[i]

            if (tx,ty) not in omoks and cnt==4:
                return (x+1,y+1)
            
    return False


white_find=search(whites_blank)
blacks_find=search(blacks_blank)

if blacks_find:
    print(1)
    print(*blacks_find)


elif white_find:
    print(2)
    print(*white_find)


else:
    print(0)

