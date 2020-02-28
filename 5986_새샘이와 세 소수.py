#어떤 크지 않은 홀수에 대해, 세 소수의 합으로 나타낼 수 있는 경우의 수를 구함
#5보다 큰 홀수 n을 입력 받아 n = x+y+z로 나타나는 경우의 수를 구하는 프로그램을 작성

def is_prime(num):
    if num != 1:
        for i in range(2, num):
            if num % i == 0:
                return False
    else:
        return False
    return num

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    prime = []

    for i in range(n):
        if is_prime(i+1):
            prime.append(i+1)
    cnt = 0

    m = len(prime)
    for i in range(m):
        for j in range(i,m):
            for k in range(j,m):
                if n == prime[i] + prime[j] + prime[k]:
                    cnt += 1

    print('#{} {}'.format(tc,cnt))





