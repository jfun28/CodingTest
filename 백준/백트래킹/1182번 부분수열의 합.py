import sys
input = sys.stdin.readline

n, s = map(int, input().split())
array = list(map(int, input().split()))
cnt = 0
answer = []

def dfs(start):
    global cnt

    print(f"[CALL] dfs({start}) | current answer = {answer}")

    if sum(answer) == s and len(answer) > 0:
        cnt += 1
        print(f"  ➤ 합이 {s}인 부분 수열 발견! -> {answer}")

    for i in range(start, n):
        answer.append(array[i])
        print(f"  ├─ append {array[i]} → answer = {answer}, next start = {i+1}")
        
        dfs(i + 1)

        popped = answer.pop()
        print(f"  └─ pop {popped} → answer = {answer} (backtrack to dfs({start}))")

dfs(0)
print(f"\n총 경우의 수: {cnt}")
