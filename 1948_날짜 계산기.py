t = int(input())

for i in range(1, t+1):
    date_list = input().split(' ') #월 일 월 일 str
    date_int = list(map(int, date_list)) #월 일 월 일 int
    first = date_int[:2] #처음 월 일 int
    second = date_int[2:] #나중 월 일 int
    calendar = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if first[0]==second[0]: #같은 월
        nth_day = second[1] - first[1] + 1

    else:
        start_month = calendar[first[0]] - first[1] #첫 월에 남은 일수
        days = start_month # 첫 월 일수

        month = second[0]-1

        while date_int[0] < month:
            days += calendar[month]
            month -= 1 # 마지막 달 까지의 일수

        final_month = second[1]

        nth_day = days + final_month +1

    print(f'#{i} {nth_day}')




