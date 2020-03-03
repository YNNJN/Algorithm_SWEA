#스택
for tc in range(10):
    a,b = input().split()
    s = []
    for ele in b:
        if len(s) == 0 or s[-1] != ele:
            s.append(ele)
        else:
            s.pop()
            continue

    print('#{}'.format(tc+1, end=' '))
    print(''.join(s))