
t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    case = 0

    for i in range(n):
        row_count = 0
        for c in range(n):
            if puzzle[i][c]:
                row_count+=1
            else :
                if row_count==k:
                    case+=1
                row_count = 0
        if row_count == k:
            case += 1

    for j in range(n):
        col_count = 0
        for r in range(n):
            if puzzle[r][j]:
                col_count+=1
            else :
                if col_count==k:
                    case+=1
                    print(r,j,case)
                col_count = 0
        if col_count == k:
            case += 1
    print(f'#{tc} {case}')
    # for i in range(n-k+1):
    #     for j in range(n-k+1):
    #         l_row, l_column = 1, 1
    #
    #         for m in range(k):
    #             l_row *= puzzle[i+m][j]
    #             if l_row == 0:
    #                 break
    #
    #         for p in range(k):
    #             l_column *= puzzle[i][j+p]
    #             if l_column == 0:
    #                 break
    #         if l_column:
    #             print(i,j)
    #         if l_row:
    #             print(i,j)
    #
    #         case += (l_row + l_column)




'''
n*n 크기의 단어 퍼즐, 단어 길이 m
단어가 들어갈 수 있는 시작 위치에 대한 범위를 먼저 정해줌
n-k+1의 범위가 되겠지
이 범위에서 1이 연속해서 k개 만큼 있는지를 찾자
행을 반복하며 찾고, 또 열을 반복하며 찾아야돼
찾으면 카운트 += 1
'''






