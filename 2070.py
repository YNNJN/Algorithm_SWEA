#2070. 큰 놈, 작은 놈, 같은 놈
#2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성



t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split(' '))

    if a > b:
        print(f'#{i} >')
    elif a == b:
        print(f'#{i} =')
    else:
        print(f'#{i} <')




