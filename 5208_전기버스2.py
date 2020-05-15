def backtrack(idx, remain, cnt):
    global n, min, stops
    remain -= 1 #다음 정류장 도착하면 배터리 감소
    if idx == n:
        if cnt < min:
            min = cnt
        return
    if cnt > min:
        return

    #배터리를 교환하고 다음 정류장으로 진행
    backtrack(idx + 1, stops[idx], cnt + 1)

    #배터리를 교환하지 않고 다음 정류장으로 진행
    if remain > 0:
        backtrack(idx + 1, remain, cnt)

for tc in range(int(input())):
    stops = list(map(int, input().split()))
    n = stops[0] #정류장 개수
    min = 10000
    backtrack(2, stops[1] , 0)
    print('#{} {}'.format(tc+1, min))



#배터리를 교환할지 말지
#출발지에서의 배터리 장착은 교환횟수에서 제외