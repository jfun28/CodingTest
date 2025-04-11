from math import sqrt

n,m=map(int,input().split())

arr=[list(map(int,input())) for _ in range(n)]

result=-1

def is_sqrt(x):
    if sqrt(x)%1==0:
        return True
    else:
        return False
        
for i in range(n):
    for j in range(m):
        for diff_x in range(-n,n):
            for diff_y in range(-m,m): # 모든 등차 간격의 모든 방향을 확인해야 최적의 정답을 찾을 수 있어.
                tmp=''
                x,y=i,j 
                if diff_x ==0 and diff_y==0:
                    continue
                while 0<=x<n and 0<=y<m:
                    tmp+=str(arr[x][y])
                    if is_sqrt(tmp):
                        result=max(result,int(tmp))
                        
                    x+=diff_x
                    t+=diff_y
                    
print(result)       