from collections import deque
money=int(input())

queue=deque()
cnt_money=0
queue.append(money)
while queue:
    money=queue.popleft()
    if money<5:
        if money%2: 
            print(-1)
            exit()

    if not money%5:
        cnt_money=cnt_money+money//5

    else:
        money=money-2
        cnt_money+=1
        queue.append(money)


print(cnt_money)