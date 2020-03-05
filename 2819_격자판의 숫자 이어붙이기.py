# #격자판이 주어질 때 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 프로그램 작성
# def dfs(r,c,num):
#     if len(num) == 7:
#         if num not in ans:
#             ans.append(num)
#         return
#
#     dr = [1, -1, 0, 0]
#     dc = [0, 0, 1, -1]
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#
#         if 0 <= nr < 4 and 0 <= nc < 4:
#             dfs(nr, nc, num + arr[nr][nc])
#
# for tc in range(int(input())):
#     arr = [input().split() for _ in range(4)]
#     ans = []
#     for i in range(4):
#         for j in range(4):
#             dfs(i,j, arr[i][j])
#
#     print('#{} {}'.format(tc+1, len(ans)))

#others - 같은 로직인데 중복을 set으로 처리하니 실행 시간이 훨씬 줄어듦, dr dc를 한 번에 처리
ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def dfs(r, c, num):
    if len(num) == 7:
        ans.add(num)
        return

    for d in ds:
        nr = r + d[0]
        nc = c + d[1]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, num + arr[nr][nc])

for tc in range(int(input())):
    arr = [list(input().split()) for _ in range(4)]
    ans = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])

    print('#{} {}'.format(tc + 1, len(ans)))