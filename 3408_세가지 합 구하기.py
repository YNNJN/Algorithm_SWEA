#8840, 제한시간초과
# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     s1, s2, s3 = 0, 0, 0
#     for i in range(1, 2*n+1):
#         if i < n+1:
#             s1 += i
#         if i % 2:
#             s2 += i
#         else:
#             s3 += i
#     print('#{} {} {} {}'.format(tc, s1, s2, s3))


#수학적
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    s1 = (n+1)*n//2
    s2 = n**2
    s3 = 2*s1
    print('#{} {} {} {}'.format(tc, s1, s2, s3))