#두 양수가 주어질 때 두 수를 더한 결과를 구하는 프로그램
t = int(input())
for tc in range(1, t+1):
    a,b = map(int, input().split())
    print('#{} {}'.format(tc, a+b))