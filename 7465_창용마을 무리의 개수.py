#두 사람이 서로 아는 관계거나 몇 사람을 거쳐서 알 수 있는 관계라면, 무리라고 함
#몇 개의 무리가 존재하는지 계산하는 프로그램 작성
def dfs(v):
    visited[v] = 1
    for e in adj[v]:
        if visited[e]: continue #continue를 추가한 것만으로 실행시간 80% 정도로 줄일 수 있음
        dfs(e)

for tc in range(int(input())):
    n,m = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    visited = [0] * (n + 1)
    cnt = 0

    for _ in range(m):
        u,v = list(map(int, input().split()))
        adj[u].append(v)
        adj[v].append(u)

    for i in range(1, len(visited)):
        if not visited[i]:
            cnt += 1
            dfs(i)

    print('#{} {}'.format(tc+1, cnt))
