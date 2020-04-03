# for tc in range(int(input())):
#     n,m = map(int, input().split())
#     c = list(map(int, input().split()))
#     arr = [[c[i], i+1] for i in range(n)]
#     i = n
#     while len(arr) > 1:
#         if arr[0][0] != 0:
#             arr[0][0] //= 2
#             if arr[0][0] == 0:
#                 arr.pop(0)
#                 if i < m:
#                     arr.append([c[i], i+1])
#                     i += 1
#             else:
#                 x = arr.pop(0)
#                 arr.append(x)
#
#     print('#{} {}'.format(tc+1, arr[0][1]))


#큐 이용
import queue
def find():
    pot = queue.Queue()
    for i in range(1, n+1):
        pot.put(i)
    idx = n + 1 #아직 화덕에 넣지 않은 피자 번호
    t = 0 #피자 인덱스
    while pot.empty() == False:
        t = pot.get()
        if arr[t]//2 != 0:
            arr[t] //= 2
            pot.put(t)
        elif idx <= m:
            pot.put(idx)
            idx += 1
    return t #마지막으로 남은 피자 번호

for tc in range(int(input())):
    n,m = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    print('#{} {}'.format(tc+1, find()))