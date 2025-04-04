n=int(input())
m = int(input())
graph=[[0]*n for i in range(n)]

# 가운데 1 채우기
x = (n - 1) // 2
y = (n - 1) // 2
graph[x][y] = 1

dx=[-1,1,0,0] #(상,하,좌,우)
dy=[0,0,-1,1]

i=2 # 채워넣을 현재의 숫자를 의미하고, 이미 1로 채워졌기 때문에 2로 시작한다
start=3 # 3*3 부터 시작해야지 뭔가 해볼수 있다.

while x!=0 or y!=0: # 1*1인 경우를 제외할 때 뺴고는 반복
    while i<=start*start:
        if x==y==(n-1)//2: # 시작점이면 cnt 세팅 후 한칸 위로
            cnt_up, cnt_down, cnt_left, cnt_right = start, start - 1, start - 1, start - 2 # 이런 식으로 중앙에서 시작해서 나선형으로 이동하면서 숫자를 채워나가는데, 각 방향마다 이동 횟수가 정해져 있어야 완전한 나선형이 됩니다. 그래서 저 카운터들이 필요한 것입니다.
            x+=dx[0]
            y+=dy[0]
            cnt_up-=1
            
        elif cnt_right > 0: # 우
            x+=dx[3]
            y+=dy[3]
            
            cnt_right-=1
            
        elif cnt_down > 0: # 하
            x+=dx[1]
            y+=dy[1]
            cnt_down-=1
            
        elif cnt_left > 0: # 좌
            x += dx[2]
            y += dy[2]
            cnt_left -= 1
            
        elif cnt_up>0 : #상
            x+=dx[0]
            y+=dy[0]
            cnt_up-=1
            
        graph[x][y]=i
        i+=1
        
    n-=2
    start+=2
    
    
for j in range(len(graph)):
    print(*graph[j])
    if m in graph[j]:
        mx=j+1
        my=graph[j].index(m)+1
    
print(mx,my)
                