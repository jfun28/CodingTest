# 1021번 회전하는 큐
import heapq
import collections


n, m=map(int,input().split())

heap=[]
find_list=[]

for i in range(n):
    heapq.heappush(heap,i+1)

heap = collections.deque(heap)

second_select=0
third_select=0

find_list=list(map(int,input().split()))
find_list = collections.deque(find_list)

while len(find_list)!=0 :
    find_num=find_list.popleft()

    if heap.index(find_num)==0:
        heap.popleft()
        continue

    if heap.index(find_num)<=len(heap)//2:
        while(1):
            f_num=heap.popleft()
            if f_num==find_num:
                break
            else:
                heap.append(f_num)
                second_select = second_select + 1

    else:
        while(1):
            if heap[0] == find_num:
                heap.popleft()
                break
            f_num = heap.pop()
            heap.appendleft(f_num)
            third_select = third_select + 1


print(second_select+third_select)