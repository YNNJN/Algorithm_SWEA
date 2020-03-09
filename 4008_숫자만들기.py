#연산자 카드를 사용하여 만들 수 있는 수식으로 얻은 결과값 중 최대값과 최소값의 차이
#재귀
def cal(i, nums):
    global max_value, min_value
    if i == n:
        max_value = max(max_value, nums)
        min_value = min(min_value, nums)
    else:
        if operator[0] != 0:
            operator[0] -= 1
            cal(i+1, nums + numbers[i])
            operator[0] += 1
        if operator[1] != 0:
            operator[1] -= 1
            cal(i+1, nums - numbers[i])
            operator[1] += 1
        if operator[2] != 0:
            operator[2] -= 1
            cal(i+1, nums * numbers[i])
            operator[2] += 1
        if operator[3] != 0:
            operator[3] -= 1
            if nums < 0 and nums % numbers[i]: #음수이면서 나누어떨어지지 않을
                cal(i+1, nums//numbers[i]+1)
            else:
                cal(i+1, nums//numbers[i])
            operator[3] += 1

for tc in range(int(input())):
    n = int(input())
    operator = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    min_value = 100000000
    max_value = -100000000
    cal(1,numbers[0])
    print(f'#{tc+1} {max_value - min_value}')