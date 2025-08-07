import sys


def z(n,r,c,res):
    length=2**n 
    half=length//2 # 사분면으로 만들기 위한 배열 길이의 절반길이 구하기
    if n==1: 
        print(2*r+c+res)
        return
    
    if r>=half and c>=half: # 4 사분면일 때 조건
        z(n-1,r-half,c-half,res+3*half*half)

    elif r>=half and c
    
