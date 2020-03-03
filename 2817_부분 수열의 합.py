#부분 수열의 합이 k가 되는 경우의 수를 출력

def combination(a, comb,k):
    cnt = 0
    for i in a:
        for j in list(comb):
            comb.append(i+j)
            if comb[-1] == k:
                cnt += 1
    return cnt

t = int(input())
for tc in range(1, t+1):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    comb = [0]
    print('#{} {}'.format(tc, combination(a, comb,k)))