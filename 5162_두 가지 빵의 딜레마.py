t = int(input())
for tc in range(1, t+1):
    a,b,c = map(int, input().split())
    min_price = a if a<b else b
    print('#{} {}'.format(tc, c//min_price))