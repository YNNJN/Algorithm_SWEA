for test_case in range(1, 11):                   #test case 1회부터 10회까지 반복
    n = int(input())                                #test case 길이 입력 받음
    building = input().split()                      #빌딩 높이 입력 받음
    building = [int(h) for h in building]
    cnt = 0                                         #count 초기화

    for i in range(2, len(building)-2):             #빌딩이 지어지지 않는 부분을 제외한 범위에서 반복

        center = building[i]                        #기준으로 삼을 가운데 빌딩 변수로 지정
        d1 = building[i - 2]                        #가장 왼쪽 끝 변수로 지정
        d2 = building[i - 1]                        #그 다음 변수로 지정
        d3 = building[i + 1]                        #기준 빌딩 오른쪽 변수로 지정
        d4 = building[i + 2]                        #그 다음 변수로 지정

        if max(center, d1, d2, d3, d4) == center:   #기준 빌딩을 포함한 양 옆 두 빌딩 중 가장 높은 것이 기준 빌딩일 조건에서

            light = center - max(d1, d2, d3, d4)    #기준 빌딩에서 그 다음으로 높은 빌딩의 높이를 뺀 것이 조망권이 확보된 세대의 수, 이를 변수로 지정
            cnt += light                            #조망권이 확보된 세대 수를 count 함

    print('#{0} {1}'.format(test_case, cnt))            #test case 회차와 조망권이 확보된 세대 수를 출력함