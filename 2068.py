#2068. 최대수 구하기
#10개 수 입력받아, 가장 큰 수 출력하는 프로그램

t = int(input())

for i in range(1, t+1):
    l = map(int, input().split(' '))

    print(f'#{i} {max(l)}')