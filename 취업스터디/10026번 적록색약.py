from collections import deque
n=int(input())

graph=[]

for _ in range(n):
    graph.append(list(input()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]



def normal_count(x,y,color):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[ny][nx]==0:
                if graph[ny][nx]==color:
                    visited[ny][nx]=1
                    queue.append((nx,ny))

          
def abnormal_count(x,y,color):
    abqueue=deque()
    abqueue.append((x,y))
    while abqueue:
        x,y=abqueue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[ny][nx]==0:
                if color=='R' or color =='G' :
                    if graph[ny][nx]=='R'or graph[ny][nx]=='G': 
                        visited[ny][nx]=1
                        abqueue.append((nx,ny))
                
                else:                    
                    if graph[ny][nx]==color:
                        visited[ny][nx]=1
                        abqueue.append((nx,ny))
          
  
            
# 정상적인 사람 시각 
n_count=0
visited=[[0]*n for i in range(n)]        
for y in range(n):
    for x in range(n):
        if visited[y][x]==0:
            n_count+=1
            visited[y][x]=1
            normal_count(x,y,graph[y][x])
            
            
# 적녹색맹 시각
ab_count=0
visited=[[0]*n for i in range(n)]        
for y in range(n):
    for x in range(n):
        if visited[y][x]==0:
            ab_count+=1
            visited[y][x]=1
            abnormal_count(x,y,graph[y][x])



       
    
print(n_count, ab_count)