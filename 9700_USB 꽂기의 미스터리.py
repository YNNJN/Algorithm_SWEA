for tc in range(int(input())):
    p,q = map(float, input().split())
    s1 = (1-p) * q
    s2 = p * (1-q) * q
    if s1 < s2:
        print('#{} YES'.format(tc+1))
    else:
        print('#{} NO'.format(tc + 1))