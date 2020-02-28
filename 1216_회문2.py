#가장 긴 회문의 길이

def is_palindrome(a):
    if a != a[::-1]:
        return False
    return True

for tc in range(1, 11):
    t = int(input())
    arr = [list(input()) for _ in range(100)]
    max_len = 0

    m = 100
    while m > 0:
        for i in range(100):
            for k in range(100-m+1):
                if is_palindrome(arr[i][k:k+m]):
                    max_len = m
                    break
        m -= 1

    m = 100
    while m > 0:
        for j in range(100):
            for k in range(100-m+1):
                temp = ''
                for i in range(k, k+m):
                    temp += arr[i][j]
                if is_palindrome(temp):
                    if max_len < len(temp):
                        max_len = len(temp)
                    break
        m -= 1
        print(m, max_len)

    print('#{} {}'.format(1, max_len))



