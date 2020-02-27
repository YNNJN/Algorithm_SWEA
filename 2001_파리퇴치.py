t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_value = 0
    temp_sum = []

    for i in range(n-m+1):
        for j in range(n-m+1):
            part_sum = 0
            for k in range(m):
                part_sum += sum(arr[i+k][j:j+m])

            temp_sum.append(part_sum)
    max_value = max(temp_sum)


    print(f'#{tc} {max_value}')





'''
i, j의 범위는 n-m+1의 행과 열에 대함
m*m 개의 인덱스, 즉 i에서 m개, i를 고정한 상태에서 j에서 m개의 값에 대해 합을 구함
구한 합을 빈 리스트에 저장하고, 그 중 최대값을 구함
'''

#2차원 배열에서 arr[i][j]로 인덱스를 한 번에 접근하려 하지 말고
#arr[i]가 리스트 형태로 주어지니, 이 상태에서 j의 변동사항을 작성하기