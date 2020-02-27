t = int(input())


for tc in range(1, t+1):
    N = input()
    arr = []

    arr = [[1 for _ in range(row)] for row in range(1, int(N)+1)] #각 행을 1로 채움
    for row in range(int(N)):

        for i in range(1, row): #각 열에 대해 반복

            sum_before = arr[row-1][i] + arr[row-1][i-1] #전 행의 i번째 수와 그 전 수의 합을 변수로 지정
            later = sum_before #이전 행 두 수의 합을 현재 행의 수로 대체
            arr[row][i] = later  # 현재 행의 i번째 수를 변수로 지정

        [print(ele,end=' ') for ele in arr[row][:-1]]
        print(arr[row][-1])


#실행시간: 0.15355s

