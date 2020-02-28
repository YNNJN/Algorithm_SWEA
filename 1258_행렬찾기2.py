def dfs(r, c):
    cnt, row_cnt = 1, 1
    stack = []
    if (r, c) in visited:
        return
    visited.append((r, c))
    stack.append((r, c))
    delta = [(0, 1), (1, 0)]
    while stack:
        r, c = stack.pop()
        for d in range(2):
            nr = r + delta[d][0]
            nc = c + delta[d][1]
            if -1 < nr < n and -1 < nc < n and arr[nr][nc] != 0 and (nr, nc) not in visited:
                if d == 1:
                    row_cnt += 1
                stack.append((nr, nc))
                visited.append((nr, nc))
                cnt += 1
    return cnt, row_cnt


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = []
    sub_arr = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                sub_arr.append(dfs(i, j))
    ans_list = []
    for i in sub_arr:
        if i:
            ans_list.append(i)
    ans_list.sort()
    result = []
    for i in ans_list:
        result.append(str(i[1]))
        result.append(str(i[0]//i[1]))
    print('#{} {}'.format(tc, len(ans_list)), end=' ')
    print(' '.join(result))