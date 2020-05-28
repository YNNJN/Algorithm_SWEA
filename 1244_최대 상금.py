def find(k):
    global ans
    if k == cnt:
        ans = max(int(''.join(arr)), ans)
        return
    for i in range(n-1):
        for j in range(i+1, n):
            arr[i], arr[j] = arr[j], arr[i]
            tmp = int(''.join(arr))
            if tmp not in visited[k+1]:
                visited[k+1].add(tmp)
                find(k+1)
            arr[i], arr[j] = arr[j], arr[i]

for tc in range(int(input())):
    number, cnt = input().split()
    cnt = int(cnt)
    arr = list(number)
    ans = 0
    n = len(arr)
    visited = [set() for _ in range(cnt+1)]
    find(0)
    print('#{} {}'.format(tc+1, ans))