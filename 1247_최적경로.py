def dfs(now, tmp, k):
    global min_value
    if tmp >= min_value:
        return
    if n == k:
        tmp += adj[now][1]
        min_value = min(min_value, tmp)
        return
    for i in range(2, n+2):
        if not visited[i]:
            visited[i] = 1
            dfs(i, tmp + adj[now][i], k+1)
            visited[i] = 0

for tc in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    g = []
    for i in range(0, len(arr), 2):
        g.append([arr[i], arr[i+1]])
    visited = [0] * (n+2)
    adj = [[0] * (n+2) for _ in range(n+2)]
    for i in range(n+2):
        for j in range(i+1, n+2):
            adj[i][j] = adj[j][i] = abs(g[i][0] - g[j][0]) + abs(g[i][1] - g[j][1])
    min_value = 10000
    dfs(0,0,0)
    print('#{} {}'.format(tc+1, min_value))