#Greedy
for tc in range(int(input())):
    n = int(input())
    schedule = []
    for _ in range(n):
        s,e = map(int, input().split())
        schedule.append([s,e])
    schedule_sort = sorted(schedule, key=lambda x:x[1])
    end = schedule_sort[0][0]
    cnt = 1
    for i in range(1,n):
        if end <= schedule_sort[i][0]:
            end = schedule_sort[i][1]
            cnt += 1
    print('#{} {}'.format(tc+1, cnt))
