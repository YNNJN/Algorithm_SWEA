def sudoku_tf(arr):
    standard = set(range(1, 10))

    for i in range(9):
        temp = set(arr[i])
        if temp == standard:
            pass
        else:
            return 0

    for j in range(9):
        temp = set()
        for i in range(9):
            temp.add(arr[i][j])
        if temp == standard:
            pass
        else :
            return 0


    for k in range(3):
        for m in range(3):
            temp = set()
            for ele in arr[3*k:3*k+3]:
                for el in ele[3*m:3*m+3]:
                    temp.add(el)
            if temp != standard:
                return 0
    return 1


t = int(input())

for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for i in range(9)]

    print(f'#{tc} {sudoku_tf(arr)}')




    #while
    #행 별, 열 별, 프랙션 별,
    #set은 add() list는 append()

