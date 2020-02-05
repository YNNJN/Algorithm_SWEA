#2071. 평균값 구하기
#10개 수 입렧받아 평균값을 출력. 소수점 첫째자리에서 반올림한 정수 출력

t = int(input())

for i in range(1, t+1):
    l = map(int, input().split(' '))
    l=list(l)

    result = sum(l)

    mean = result/len(l)
    new_mean = round(mean)



    print(f'#{i} {new_mean}')