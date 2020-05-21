def dfs(v):
    global n, cnt
    for i in range(n):
        if not visited[i]:
            if graph[v][i]:
                visited[i] = 1
                dfs(i)

for tc in range(int(input())):
    n,m = map(int, input().split())
    pairs = list(map(int, input().split()))
    graph = [[0 for _ in range(n)] for _ in range(n)]
    visited = [0] * n
    cnt = 0

    for i in range(0, len(pairs), 2):
        r = pairs[i] - 1
        c = pairs[i + 1] - 1
        graph[r][c] = 1
        graph[c][r] = 1

    for i in range(n):
        if not visited[i]:
            cnt += 1
            dfs(i)
    print('#{} {}'.format(tc+1, cnt))
