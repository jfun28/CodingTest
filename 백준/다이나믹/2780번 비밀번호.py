import sys
input=sys.stdin.readline

t=int(input())
answer=[]
for _ in range(t):
    password=[1]*10
    n=int(input())

    for i in range(1,n):
        curPass=password.copy()
        # 길이가 N인 비밀번호의 갯수는 인접한 숫자의 길이가 N_1인 비밀번호 조합수와 같다. 
        password[0]=curPass[7]
        password[1]=curPass[2]+curPass[4]
        password[2]=curPass[1]+curPass[3]+curPass[5]
        password[3]=curPass[2]+curPass[6]
        password[4]=curPass[1]+curPass[5]+curPass[7]
        password[5]=curPass[2]+curPass[4]+curPass[6]+curPass[8]
        password[6]=curPass[3]+curPass[5]+curPass[9]
        password[7]=curPass[4]+curPass[8]+curPass[0]
        password[8]=curPass[7]+curPass[5]+curPass[9]
        password[9]=curPass[6]+curPass[8]

    answer.append(sum(password)%1,234,567)
 
for i in answer:
    print(i)


