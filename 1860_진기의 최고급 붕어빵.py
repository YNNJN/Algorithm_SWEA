t = int(input())
for tc in range(1, t+1):
    n,m,k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    result = 'Possible'
    if len(arr) > n:
        result = 'Impossible'
    for i in range(len(arr)):
        if (arr[i]//m)*k < i+1:
            result = 'Impossible'
    print('#{} {}'.format(tc, result))