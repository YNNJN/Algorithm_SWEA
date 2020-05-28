def dij(n):
    inf = float('inf')
    d = [inf] * (n+1)
    d[0] = 0
    visited = [0] * (n+1)
    c = 0

    while c < n:
        min_value = inf
        min_idx = 0
        for i in range(n+1):
            if visited[i] == 0 and d[i] < min_value:
                min_idx = i
                min_value = d[i]
        visited[min_idx] = 1
        for x, wt in adj[min_idx]:
            if d[x] > d[min_idx] + wt:
                d[x] = d[min_idx] + wt
        c += 1
    return d[n]

for tc in range(int(input())):
    n,e = map(int, input().split())
    adj = {i: [] for i in range(n+1)}
    for i in range(e):
        s,e,w = map(int, input().split())
        adj[s].append([e,w])
    print('#{} {}'.format(tc+1, dij(n)))





# for tc in range(int(input())):
#     n,e = map(int, input().split())
#     graph = {i:[] for i in range(n+1)}
#     for _ in range(e):
#         s,e,w = map(int, input().split())
#         graph[s].append((e,w))
#
#     inf = float('inf')
#     d = [inf] * (n+1)
#     p = [None] * (n+1)
#     visited = [False] * (n+1)
#     d[0] = 0
#     cnt = 0
#
#     while True:
#         min = inf
#         u = -1
#         for i in range(n+1):
#             if not visited[i] and d[i] < min:
#                 min = d[i]
#                 u = i
#         visited[u] = True
#         if u == n: break
#         for (j,k) in graph[u]:
#             if not visited[j] and d[u] + k < d[j]:
#                 d[j] = d[u] + k
#                 p[j] = u
#
#     print('#{} {}'.format(tc+1, d[n]))

