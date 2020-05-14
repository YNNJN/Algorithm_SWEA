# 시간 초과
# def check(num):
#     divs = [i for i in range(1, num + 1) if num % i == 0]
#     odds = [div for div in divs if div % 2 == 1]
#     return odds
#
# for tc in range(int(input())):
#     l,r = map(int, input().split())
#     nums = list(range(l, r+1))
#     ans = 0
#     for num in nums:
#         ans += sum(check(num))
#     print('#{} {}'.format(tc+1, ans))



#DP 문제였다......

#모든 약수의 합을 구해놓는 배열 만들기
f = [0] * 1000001

#i의 약수 중 홀수의 합
for i in range(1, 1000001, 2):
    for j in range(i, 1000001, i):
        f[j] += i

#1~i까지 약수 중 홀수의 합
for i in range(1, 1000000):
    f[i + 1] += f[i]

#범위 내 약수 && 홀수의 합
for tc in range(int(input())):
    l,r = map(int, input().split())
    print('#{} {}'.format(tc+1, f[r] - f[l-1]))