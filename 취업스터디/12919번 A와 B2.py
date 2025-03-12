s = input()
t = input()
 
def dfs(x):
    if len(x) == len(s):
        if x == s:
            print(1)
            exit()
        else:
            return
    if x[-1] == 'A':
        dfs(x[:-1])
    if x[0] == 'B':
        dfs(x[::-1][:-1])
    return
        
dfs(t)
print(0)