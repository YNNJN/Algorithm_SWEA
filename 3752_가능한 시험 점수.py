#학생들이 받을 수 있는 점수의 경우의 수를 출력

#M3
for tc in range(int(input())):
    n = int(input())
    prb = list(map(int, input().split()))
    scr = {0}
    for i in prb:
        for j in list(scr):
            scr.add(j+i)
    print('#{} {}'.format(tc+1, len(scr)))


# # M4
# for tc in range(int(input())):
#     n = int(input())
#     prb = list(map(int, input().split()))
#     scr = [0] * (sum(prb) + 1)
#     scr[0] = 1
#     for j in range(n):
#         for i in range(sum(prb), -1, -1):
#             if scr[i]:
#                 scr[prb[j] + i] = 1
#
#     print('#{} {}'.format(tc+1, sum(scr)))


# #비트마스크
# for tc in range(int(input())):
#     n = input()
#     prb = map(int, input().split())
#     scr = 1
#     for i in prb:
#         scr |= scr << i
#     print('#{} {}'.format(tc+1, bin(scr).count('1')))



# #dfs
# def dfs(depth, sum):
#     global result
#     if depth == n:
#         result.add(sum)
#         return
#     for i in range(n):
#         dfs(depth + 1, sum + prb[i])
#         dfs(depth + 1, sum)
#
# for tc in range(int(input())):
#     n = int(input())
#     prb = list(map(int, input().split()))
#     scr = set()
#     scr.add(0)
#     for i in range(n):
#         temp = []
#         for num in scr:
#             temp.append(prb[i] + num)
#         for t in temp:
#             scr.add(t)
#
#     print('#{} {}'.format(tc+1, len(scr)))

