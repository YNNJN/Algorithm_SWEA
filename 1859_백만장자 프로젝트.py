'''
맥스 전까진 일단 사, 그리고 맥스에서 팔아
맥스 다음은 슬라이싱한 다음, 그 중 맥스를 구하고 그 전까진 사고 또 맥스에서 팔아
재귀의 향기
'''

import sys
sys.stdin = open('input17.txt','r')


def trick(sales):
    if len(sales) in [1,0]:
        return 0

    ans, profit = 0, 0
    max_idx = sales.index(max(sales))

    for sale in sales[:max_idx]:
        ans -= sale

    profit = max_idx * max(sales) + ans

    if max_idx < len(sales)-1:
        profit += trick(sales[max_idx+1:])

    return profit


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    sales = list(map(int, input().split()))

    print(f'#{tc} {trick(sales)}')
