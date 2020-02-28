# #제한시간초과 #재귀
# def sequence(n):
#     if n <= 2:
#         return 1
#     else:
#         return sequence(n-3) + sequence(n-2)
#
# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())-1
#     print('#{} {}'.format(tc, sequence(n)))


# #더 작게 잘라서
# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())-1
#     s = [1, 1, 1, 2, 2]
#
#     for i in range(5, n+1):
#         s.append(s[i-1] + s[i-5])
#
#     print('#{} {}'.format(tc, s[-1]))



n = 100
s = [0 for _ in range(n + 1)]
for i in range(1, n+1):
    if i < 4:
        s[i] = 1
    else:
        s[i] = s[i - 3] + s[i - 2]

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    print('#{} {}'.format(tc, s[n]))