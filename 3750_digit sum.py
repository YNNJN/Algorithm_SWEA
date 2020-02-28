# #제한시간 초과 #재귀
# def digit_sum(n):
#     s = 0
#     for i in range(len(n)):
#         s += int(n[i])
#     if len(str(s)) == 1:
#         return s
#     else:
#         n = str(s)
#         return digit_sum(n)
#
# t = int(input())
# for tc in range(1, t+1):
#     n = input()
#     print('#{} {}'.format(tc, digit_sum(n)))


# 수학적 아이디어
# ans = list()
# for tc in range(int(input())):
#     nums = input()
#     f = list(range(1, 10))
#     if int(nums) < 10:
#         ans.append(int(nums))
#     else:
#         sum = 0
#         for i in range(len(nums)):
#             sum += int(nums[i])
#         if sum >= 10:
#             result = f[(sum % 9) - 1]
#             ans.append(result)
#         else:
#             result = sum
#             ans.append(result)
# j = 1
# for i in ans:
#     print('#{} {}'.format(j,i))
#     j += 1


#노멀
ans = []
for tc in range(int(input())):
    n = input()

    while True:
        if len(n) == 1:
            ans.append(n)
            break
        else:
            result = []
            for i in n:
                result.append(int(i))
            n = str(sum(result))
j = 1
for i in ans:
    print('#{} {}'.format(j, i))
    j += 1


