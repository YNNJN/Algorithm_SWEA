#2056. 연월일 달력
#날짜 유효성 판단해서 연/월/일 8자리 끊어서 출력해주기, 아니면 -1 출력
#월은 1~12, 날짜는 각 달의 마지막 날 안에 들어와야 유효한 것


t = int(input())

for i in range(1, t + 1):

    num = input()
    year = num[0:4]
    month = num[4:6]
    day = num[6:8]
    day_i = int(num[6:8])
    calendar = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}

    months = calendar.keys()

    if month in months:
        days = calendar[month]

        if day_i in range(1, days + 1):
            print(f'#{i} {year}/{month}/{day}')

        else:
            print(f'#{i} -1')

    else:
        print(f'#{i} -1')
