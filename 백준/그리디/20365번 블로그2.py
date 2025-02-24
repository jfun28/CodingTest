# 컬러의 갯수를 세는게 아니라 몇번의 구간이 바뀌었는지 세는것이 핵심이다.

n=int(input())

colors=input()

cdict={'B':0, 'R':0}
precolor=''

for color in colors:
    if color!=precolor:
        cdict[color]+=1

    precolor=color

count=cdict['R']+1 if cdict['B']>cdict['R'] else cdict['B']+1

print(count)
