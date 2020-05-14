#는 아직 시간 초과 코드
#문자열 다루던 부분 정수형으로 고쳐야지

def ten2nine(num):
    new_num = ''
    for i in num:
        if int(i) >= 4:
            new_num += str(int(i) - 1)
        else:
            new_num += i
    return new_num

def nine2ten(num):
    n = len(num)
    new_num = 0

    j = 0
    for i in range(n-1, -1, -1):
        new_num += int(num[i] * 9 ** j)
        j += 1

    return new_num


for tc in range(int(input())):
    a,b = input().split()

    a_min, b_min = False, False

    if a[0] == '-':
        a_min = True
        a = a[1:]
    if b[0] == '-':
        b_min = True
        b = b[1:]

    a = ten2nine(a)
    a = nine2ten(a)
    b = ten2nine(b)
    b = nine2ten(b)

    if a_min: a = -a
    if b_min: b = -b

    if a_min == b_min:
        print('#{} {}'.format(tc+1, b - a))
    else:
        print('#{} {}'.format(tc+1, b - a - 1))



    #4를 뺀 층의 개수
    #0이 사이에 있으면 - 1
    #tc1. 1- -1 - 1
    #tc2. 3- -5 - 1 - 1

    #입력받은 수를 9진수 취급하자
    #1, 2, 3, 5, 6, 7, 8, 9, 0
    #=> 1, 2, 3, 4, 5, 6, 7, 8, 0
    #각 자리수에 대해 4보다 크면 1을 빼고, 아니면 원래의 수


