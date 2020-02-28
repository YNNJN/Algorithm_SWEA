#l분 이상 u분 이하의 운동, 이번주 x분 함
def exercise(l, u, x):
    if x > u:
        return -1
    elif x >= l:
        return 0
    else:
        return l-x

t = int(input())
for tc in range(1, t+1):
    l,u,x = map(int, input().split())
    print('#{} {}'.format(tc, exercise(l, u, x)))
