# t = int(input())
# for tc in range(1, 11):
#     data = list(map(int, input().split()))
#     flag = True
#     while flag:
#         for i in range(1,6):
#             temp = data[0] #이동시키고 난 다음의 처리를 해줘야
#             for j in range(len(data)-1):
#                 data[j] = data[j+1]
#                 data[-1] = temp-i
#                 if data[-1] > 0:
#                     pass
#                 else:
#                     data[-1] = 0
#                     flag = False
#
#     print('#{} {}'.format(tc, ' '.join(map(str, data))))


# n = 8
# for t in range(1, 11):
#     tc = int(input())
#     nums = list(map(int, input().split()))
#     flag = 1
#     while flag:
#         for i in range(1, 6):
#             tmp = nums[0]
#             for j in range(1, n):
#                 nums[j-1] = nums[j]
#             nums[-1] = tmp - i
#             if nums[-1] < 1:
#                 nums[-1] = 0
#                 flag = 0
#                 break
#     print('#{0}'.format(t), end=' ')
#     for num in nums:
#         print(num, end=' ')


# #queue 이용
# for _ in range(1, 11):
#     tc = int(input())
#     que = list(map(int, input().split()))
#     dist = 0
#     while True:
#         num = que.pop(0)
#         dec = dist % 5 + 1 #감소하는 숫자가 1, 2, 3, 4, 5, 다시 1로 변함
#         num -= dec
#         if num <= 0:
#             que.append(0)
#             break
#         que.append(num)
#         dist += 1
#     print('#{}'.format(tc), end =' ')
#     print(' '.join(map(str, que)))


#젤 간단, 0의 개수 세서 풀기
for t in range(10):
    n = int(input())
    data = list(map(int, input().split()))

    while data.count(0) != 1:
        for i in range(1, 6):
            a = data.pop(0) - i
            if a <= 0:
                a = 0
            data.append(a)
            if data.count(0) >= 1:
                break

    print('#{} {}'.format(t+1, ' '.join(list(map(str, data)))))