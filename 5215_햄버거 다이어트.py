def func(food, cal): #info, 1000)
    if cal < food[0][1]:
        return 0
    if len(food) == 1 :
        if cal > food[0][1]:
            return food[0][0]

    take_0 = food[0][0] + func(food[1:], cal-food[0][1])
    no_take_0 = func(food[1:], cal)

    if take_0 > no_take_0 :
        return take_0
    else:
        return no_take_0


#그리디알고리즘

t = int(input())
for tc in range(1, t+1):
    n,l = map(int, input().split())
    info = []
    for _ in range(n):
        t,k = map(int, input().split())
        info.append([t,k])
        t_sum, k_sum, max_value = 0, 0, 0

    for i in range(len(food)):
        food = sorted(info, reverse=True)
        for i in range(len(food)):
            while cal <= l:
                t_sum += t_list[i][0]
                k_sum += t_list[i][1]
            if max_value < t_sum:
                max_value = t_sum

            print(t_sum, k_sum, max_value)



'''
def dfs(i,s,c):
    global max_score
    if c > l:
        return
    if i == n:
        if s > max_score:
            max_score = s
    if i > n-1:
        return

    dfs(i+1, s+score[i], c+cal[i])
    dfs(i+1, s, c)
    return max_score

t = int(input())
for tc in range(1, t+1):
    n, l = map(int, input().split())
    score = []
    cal = []
    max_score = 0
    for _ in range(n):
        t, k = map(int, input().split())
        score.append(t)
        cal.append(k)
    print('#{} {}'.format(tc, dfs(0,0,0)))
'''

