def is_palindrome(a):
    for i in range(8):
        if a != a[::-1]:
            return False
    return True

for tc in range(1, 11):
    m = int(input())
    arr = [list(input()) for _ in range(8)]
    cnt = 0

    for i in range(8):
        for k in range(8-m+1):
            if is_palindrome(arr[i][k:k+m]):
                cnt += 1

    for j in range(8):
        for k in range(8-m+1):
            temp =''
            for i in range(k, k+m):
                temp += arr[i][j]
            if is_palindrome(temp):
                cnt += 1

    print('#{} {}'.format(tc, cnt))
