from collections import deque
queue=deque()

def solution(numbers, target):
    leaves=[0]
    count=0
    queue.append(numbers)
    print("queue",queue)
    while queue:
        num=queue.popleft()
        temp=[]

        # 자손 노드
        for leaf in leaves:
            temp.append(leaf+num)
            temp.append(leaf-num)

        leaves=temp

    for leaf in leaves:
        if leaf==target:
            count+=1

    return count, leaves

count, leaves=solution([1, 1, 1, 1, 1], 3)

print("leaves", leaves)
print("count", count)