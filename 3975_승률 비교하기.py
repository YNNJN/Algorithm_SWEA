# t = int(input())
# for tc in range(1, t+1):
#     case = list(map(int, input().split()))
#     a = case[0]/case[1]
#     b = case[2]/case[3]
#     if a == b:
#         print('#{} {}'.format(tc, 'DRAW'))
#         continue
#     win = 'ALICE' if (a > b) else 'BOB'
#     print('#{} {}'.format(tc, win))




ans = []
t = int(input())
for _ in range(t):
    a,b,c,d = map(int, input().split())
    ans.append('ALICE' if a/b>c/d else 'DRAW' if a/b==c/d else 'BOB')
for i in range(t):
    print(f'#{i+1} {ans[i]}')