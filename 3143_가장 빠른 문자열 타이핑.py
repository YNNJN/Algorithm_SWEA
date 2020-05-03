def scan(a, b):
    idx = 0
    cnt = 0
    while idx < len(a):
        if a[idx:idx+len(b)] == b:
            idx += len(b)
        else:
            idx += 1
        cnt += 1
    return cnt

for tc in range(int(input())):
    a, b = input().split()
    print('#{} {}'.format(tc+1, scan(a,b)))




