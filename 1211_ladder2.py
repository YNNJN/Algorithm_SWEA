def search(r, c, arr):
    dr = [0, 0, 1]
    dc = [1, -1, 0]
    direc = ['l','r','d']
    cnt = 1
    now_r, now_c = r, c
    visited = [] # 지나온 (r,c) 저장
    while now_r < 99:
        for i in range(3):  #새로운 좌표를 계산함
            tr = now_r + dr[i]
            tc = now_c + dc[i]

            if tr < 0 or tc < 0 or tr > n-1 or tc > n-1:  #범위 안인지
                pass
            elif arr[tr][tc] == 0:  #사다리 위인지
                pass
            elif (tr,tc) in visited :  #이미 지나온 곳인지
                pass

            else: #갈 수 있다면
                visited.append( (tr,tc) )
                cnt += 1
                now_r = tr
                now_c = tc
                #print(direc[i],now_r,now_c, cnt)
                break
    return cnt

for tc in range(1, 11):
    t = int(input())
    n = 100
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 100 * 100  #최대값으로 미리 설정
    minIdx = 0

    for j in range(n):
        if arr[0][j] == 1:  #i는 시작점
            cnt = search(0, j, arr)
            if ans > cnt:
                ans = cnt
                minIdx = j

    print('#{} {}'.format(tc, minIdx))
