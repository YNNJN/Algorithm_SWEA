#10개 수를 입력 받아 최대 수와 최소 수를 제외한 나머지의 평균값 출력
#(소수 첫째 자리에서 반올림한 정수를 출력)

t = int(input())

for tc in range(1, t+1):
    case = list(map(int, input().split()))
    case.remove(max(case))
    case.remove(min(case))
    avg = round(sum(case)/len(case))

    print(f'#{tc} {avg}')