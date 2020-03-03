t = int(input())
for tc in range(1, t+1):
    a,b = map(int, input().split())
    s = a//b
    print('#{} {}'.format(tc, s**2))

# #오 이런 예외처리가 필요했군,,,,,
#     if B > A//2:
#         ans = 1
