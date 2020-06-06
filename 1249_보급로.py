from collections import deque

def bfs():
    while q:
        x,y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] or dist[nx][ny] > dist[x][y] + arr[nx][ny]:
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + arr[nx][ny]
                    q.append((nx, ny))

for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    dist = [[0 for _ in range(n)] for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append((0,0))
    dist[0][0] = arr[0][0]
    visited[0][0] = 1
    bfs()
    print('#{} {}'.format(tc + 1, dist[n - 1][n - 1]))
