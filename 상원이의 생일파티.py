from collections import deque

def bfs(q):
    global ans
    while q:
        idx, depth = q.popleft()
        for i in tree[idx]:
            if not visited[i]:
                visited[i] = 1
                ans += 1
                if depth < 1:
                    q.append((i, depth+1))

for tc in range(int(input())):
    ans = 0
    n,m = map(int, input().split())
    tree = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for _ in range(m):
        a,b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    q = deque()
    q.append((1,0))
    visited[1] = 1
    bfs(q)
    print('#{} {}'.format(tc+1, ans))