# 자물쇠와 열쇠

def rotate(key): # 사각형을 90도 회전하는 함수
    n=len(key)
    result=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n-i-1]=key[i][j] # 행과 열이 바뀌는 거 아는거에 피지컬이 조금 들어감
    return result

def check(lock):
    n=len(lock)//3
    for i in range(n,n*2):
        for j in range(n,n*2):
            if lock[i][j] !=1:
                return False
    return True

def solution(key,lock):
    n=len(lock)
    m=len(key)
    new_lock=[[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n]=lock[i][j]
    
    for rotation in range(4):
        key=rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[i+x][j+y]+=key[i][j] # 자물쇠와 열쇠가 맞춰보는 과정이므로 'x','y'는 자물쇠 위에서 열쇠를 맞춰보는 시작위치, i와 j는 열쇠의 각 칸을 나타낸다
                if check(new_lock)==True:
                    return True
                else:
                    for i in range(m):
                        for j in range(m):
                            new_lock[i+x][j+y]-=key[i][j]

    return False

                

