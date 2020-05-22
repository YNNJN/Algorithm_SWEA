# # dfs
# def dfs(v):
#     global n, cnt
#     for i in range(n):
#         if not visited[i]:
#             if graph[v][i]:
#                 visited[i] = 1
#                 dfs(i)
#
# for tc in range(int(input())):
#     n,m = map(int, input().split())
#     pairs = list(map(int, input().split()))
#     graph = [[0 for _ in range(n)] for _ in range(n)]
#     visited = [0] * n
#     cnt = 0
#
#     for i in range(0, len(pairs), 2):
#         r = pairs[i] - 1
#         c = pairs[i + 1] - 1
#         graph[r][c] = 1
#         graph[c][r] = 1
#
#     for i in range(n):
#         if not visited[i]:
#             cnt += 1
#             dfs(i)
#     print('#{} {}'.format(tc+1, cnt))


def rep(n): #find_set
    while p[n] != n:
        n = p[n]
    return n

for tc in range(int(input())):
    n,m = map(int,input().split())
    l = list(map(int,input().split()))
    p = [i for i in range(n+1)] # make_set

    for i in range(m):
        a = l[2*i]
        b = l[2*i+1]
        p[rep(b)] = rep(a) # union # b집합의 대표를 a의 대표로 교체함
    cnt = 0
    for i in range(1, n+1): # 대표자의 수 찾기
        if p[i] == i:
            cnt += 1
    print('#{} {}'.format(tc+1, cnt))