for tc in range(10):
    a = int(input())
    b = list(map(int, input().split()))
    c = int(input())
    d = list(input().split())
    for i in range(len(d)):
        if d[i] == 'I':
            idx = int(d[i + 1])
            nums = int(d[i + 2])
            for j in range(nums):
                b.insert(idx+j, int(d[i+2+(j+1)]))
        elif d[i] == 'D':
            idx = int(d[i + 1])
            nums = int(d[i + 2])
            for j in range(nums):
                del b[idx]
        elif d[i] == 'A':
            nums = int(d[i + 1])
            for j in range(nums):
                b.append(d[i + 2 + j])
        else:
            continue
    print('#{} {}'.format(tc+1,' '.join(map(str, b[:10]))))