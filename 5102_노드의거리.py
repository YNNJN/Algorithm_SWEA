def bfs(s):
    global result
    q.append(s)
    visited[s] = 1

    while q:
        s = q.pop(0)
        for ns in range(1, v+1):
            if adj[s][ns] and not visited[ns]:
                q.append(ns)
                visited[ns] = 1
                cnt_list[ns] = cnt_list[s] + 1
                if ns == g:
                    result = cnt_list[ns]
                    return
    return

for tc in range(int(input())):
    v,e = map(int, input().split())
    adj = [[0] * (v + 1) for _ in range(v + 1)]
    visited = [0] * (v + 1)
    cnt_list = [0] * (v + 1)

    for i in range(e):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = adj[n2][n1] = 1

    s,g = map(int, input().split())

    q = []
    result = 0
    bfs(s)
    print('#{} {}'.format(tc+1, result))