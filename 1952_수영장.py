#계획대로 이용하는 경우 가장 적은 비용으로 수영장을 이용할 수 있는 비용 출력
def find(n, s, d, m, m3):
    global min_value
    if n > 12:
        if min_value > s:
            min_value = s
        else: return #백트래킹
    else:
        find(n+1, s+plan[n]*d, d, m, m3)
        find(n+1, s+m, d, m, m3)
        find(n+3, s+m3, d, m, m3)


for tc in range(int(input())):
    d, m, m3, y = map(int, input().split())
    plan = [0] + list(map(int, input().split())) #n월 이용일
    min_value = y
    find(1, 0, d, m, m3)
    print('#{} {}'.format(tc+1, min_value))

