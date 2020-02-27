def rotate(arr):
    n = len(arr)
    arr_copy = [[0 for i in range(n)] for j in range(n)]

    for i in range(len(arr)):
        for j in range(len(arr)):

            arr_copy[j][n-1-i] = arr[i][j]

    return arr_copy


t = int(input())

for tc in range(1, t+1):
    print(f'#{tc}')
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]


    rotate_90 = rotate(arr)
    rotate_180 = rotate(rotate_90)
    rotate_270 = rotate(rotate_180)

    for p in range(n):
        tmp=rotate_90[p]+['-']+rotate_180[p]+['-']+rotate_270[p]
        for ele in tmp:
            if ele=='-': print(' ',end='')
            else : print(ele,end='')
        print()



#리스트를 리스트에 어펜드->리스트가 원소로서 들어감
#arr의 len는 행의 개수가 출력됨
#출력의 꼴을 맞출 때, 출력은 항상 줄 단위로 되니까, 해당 줄에서 어떻게 조작할지 생각할 것