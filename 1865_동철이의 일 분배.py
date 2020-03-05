#주어진 일이 모두 성공활 확률의 최대값
def dfs(v,s):
    global max_p
    if s == 0 or s <= max_p: #s는 확률이므로 곱할수록 작아지니
        return
    if v == n:
        if max_p < s:
            max_p = s
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(v+1, s * p[v][i] * 0.01)
            visited[i] = 0

for tc in range(int(input())):
    n = int(input())
    p = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    max_p = 0
    dfs(0,1)
    print('#{} {:.6f}'.format(tc+1, max_p * 100))
