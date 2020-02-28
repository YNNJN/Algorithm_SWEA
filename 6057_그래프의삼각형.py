t = int(input())
for tc in range(1,t+1):
    v,e = map(int, input().split())
    adj = [[0 for _ in range(v + 1)] for _ in range(v + 1)]
    for _ in range(e):
        x,y = map(int, input().split())
        adj[x][y] = 1
        adj[y][x] = 1


    cnt = 0
    for i in range(1,v+1):
        adj_list = []
        for j in range(1,v+1):
            if adj[i][j] == 1:
                adj_list.append(j)
        for j1 in range(len(adj_list)):
            for j2 in range(len(adj_list)):
                if adj[adj_list[j1]][adj_list[j2]] == 1:
                    cnt += 1
    print('#{} {}'.format(tc, cnt//6))


    '''
    하나의 노드에 대한 간선의 경우의 수를 구하고
    그 중 둘이 연결되어있는지를 따져서 카운트
    '''