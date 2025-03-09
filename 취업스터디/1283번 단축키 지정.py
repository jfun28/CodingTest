import sys
input=sys.stdin.readline
n=int(input())
arr=[] # 단축기로 지정된 알파벳벳

for _ in range(n):
    word=list(map(str,input().split()))

    # 1번과 2번의 방법을 수행
    for i in range(len(word)):
        # 현재 단어의 첫 글자가 단축키로 지정되어 있지 않다면
        if word[i][0].upper() not in arr:
            arr.append(word[i][0].upper()) # 현재 단어의 첫 글자를 단축키로 지정

            word[i]="["+word[i][0]+"]"+word[i][1:]
            print(" ".join(word))
            break
    
        # 반복문이 break를 통과하지 않을때
    else:
        # 3번의 방법을 수행
        for j in range(len(word)): # 단어 묶음으로 되어 있는 확인 반복문문
            flag=False # 현재 단어의 알파벳을 단축축키로 사용했는지 유무
            # 반복문을 통해 모든 단어의 알파벳을 확인
            for k in range(len(word[j])):
                # 현재 단어의 알파벳이 단축키로 지정되어 있지 않다면
                if word[j][k].upper() not in arr:
                    arr.append(word[j][k].upper()) # 현재 단어의 첫 글자를 단축키로 지정

                    flag=True

                    word[j]=word[j][:k]+'['+word[j][k]+']'+word[j][k+1:]
                    print(" ".join(word))

                    break


            if flag: # 이게 없으면은 "H[e]lp M[e] Pl[e]ase"일 때 3개 단축키가 형성된다. 
                break

        else:
            print(*word) 


