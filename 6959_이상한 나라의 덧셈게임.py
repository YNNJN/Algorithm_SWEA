
for tc in range(int(input())):
    n = input()
    cnt = 0

    while len(n) > 1:
        n = n.replace(n[0:2], str(int(n[0]) + int(n[1])), 1) #n.replace(self, old, new, count)
        cnt += 1
    if cnt % 2: winner = 'A'
    else: winner = 'B'

    print('#{} {}'.format(tc+1, winner))



# for tc in range(int(input())):
#     stack = list(map(int, input()))
#     cnt = 0
#     while len(stack) > 1:
#         a = stack.pop()
#         b = stack.pop()
#         new_number = a + b
#         if a + b < 10:
#             stack.append(new_number)
#         else:
#             stack.append(new_number // 10)
#             stack.append(new_number % 10)
#         cnt += 1
#
#     if cnt % 2: winner = 'A'
#     else: winner = 'B'
#     print('#{} {}'.format(tc+1, winner))
