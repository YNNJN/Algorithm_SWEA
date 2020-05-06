def find(current):
    global min_value, sum_value
    if min_value > sum_value:
        visited[current] = 1

        if 0 not in visited:
            sum_value += board[current][0]
            if min_value > sum_value:
                min_value = sum_value
            sum_value -= board[current][0]

        else:
            for next in range(n):
                if visited[next] == 0:
                    sum_value += board[current][next]
                    find(next)
                    sum_value -= board[current][next]
        visited[current] = 0

for tc in range(int(input())):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    min_value, sum_value = 100000, 0
    find(0)
    print('#{} {}'.format(tc+1, min_value))

