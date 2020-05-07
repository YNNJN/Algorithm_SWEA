#Greedy #역순으로 생각
for tc in range(int(input())):
    n,m = map(int, input().split())
    w = list(map(int, input().split())) #n개
    t = list(map(int, input().split())) #m개

    w.sort()
    t.sort()
    ans = 0
    for _ in range(min(n,m)):
        if w[-1] > t[-1]:
            w.pop()
        else:
            ans += w.pop()
            t.pop()
    print('#{} {}'.format(tc+1, ans))

