# # 시간초과
# def bfs(x,y):
#     q = []
#     visited = [0] * 1000001
#     q.append((x,0))
#
#     while q:
#         now, cnt = q.pop(0)
#         if now == y:
#             return cnt
#
#         for i in range(4):
#             tmp = now
#             if i == 0:
#                 tmp += 1
#             elif i == 1:
#                 tmp -= 1
#             elif i == 2:
#                 tmp *= 2
#             else:
#                 tmp -= 10
#
#             if 0 < tmp <= 10 ** 6 and not visited[tmp]:
#                 visited[tmp] = 1
#                 q.append((tmp, cnt + 1))
#
# for tc in range(int(input())):
#     n,m = map(int, input().split())
#     ans = bfs(n,m)
#     print('#{} {}'.format(tc+1, ans))

'''
덱 이용하기!!!

deque(덱)
double-ended queue
앞과 뒤 양방향에서 데이터를 처리할 수 있는 구조
데이터 처리속도가 빠름(이중연결리스트로 구현)

- append(x): 덱의 가장 뒤에 x를 삽입한다.
- appendleft(x): 덱의 가장 앞에 x를 삽입한다.
- pop(): 덱의 가장 마지막 원소를 제거하며 반환한다.
- popleft(): 덱의 가장 처음 원소를 제거하며 반환한다.

'''

from collections import deque

def bfs(n,m):
    v = {n:1}
    # q = [n]
    q = deque()
    q.append(n)

    while q:
        n = q.popleft()
        t = [n-10,n-1,n+1,n*2]
        for i in range(4):
            if t[i] == m:
                return v[n]
            if t[i] > 0 and t[i] <= 1000000:
                if v.get(t[i]) == None:
                    v[t[i]] = v[n] + 1
                    q.append(t[i])

for tc in range(int(input())):
    n,m = map(int,input().split())
    print('#{} {}'.format(tc+1, bfs(n,m)))
