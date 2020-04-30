# for tc in range(int(input())):
#     n, m = map(str, input().split())
#     num = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
#     ans = ''
#     for i in m:
#         if i == 'A':
#                 ans += num[10]
#         elif i == 'B':
#                 ans += num[11]
#         elif i == 'C':
#                 ans += num[12]
#         elif i == 'D':
#                 ans += num[13]
#         elif i == 'E':
#                 ans += num[14]
#         elif i == 'F':
#                 ans += num[15]
#         else:
#             ans += num[int(i)]
#     print('#{} {}'.format(tc+1, ans))



# trans = {'0': 0,'1': 1, '2': 2, '3': 3, '4': 4,'5': 5,'6': 6,'7': 7,'8': 8, '9': 9, 'A': 10,'B': 11,'C': 12, 'D': 13,'E': 14,'F': 15}
#
# def binary(num):
#     global tmp
#     for i in range(4):
#         div = num // 2
#         mod = num % 2
#         tmp = str(mod) + tmp
#         num = div
#     return tmp
#
# for tc in range(int(input())):
#     n,m = map(str, input().split())
#     ans = ''
#     for i in m:
#         tmp = ''
#         ans += binary(trans[i])
#     print('#{} {}'.format(tc+1, ans))



#비트연산
for tc in range(int(input())):
    n, hex_digit = map(str,input().split())
    n = int(n)
    result = ''
    for i in range(n):
        for j in range(3, -1, -1):
            if int(hex_digit[i], 16) & 1 << j:
                result += '1'
            else:
                result += '0'
    print('#{} {}'.format(tc+1, result))

