t = int(input())

for tc in range(1, t+1): #테스트케이스 t회 반복
    N, k = map(int, input().split()) #학생 수와 학점을 알고 싶은 학생의 번호 k 입력
    totalscr_list = []  #전체 점수를 담을 리스트 초기화

    for n in range(N): #학생 수 만큼에 대해
        scr_mid, scr_fin, scr_ass = map(int, input().split()) #점수를 입력받음
        scr_total = 0.35*scr_mid + 0.45*scr_fin + 0.2*scr_ass #반영 비율 고려한 총 점수 계산
        totalscr_list.append(scr_total) #각 학생의 점수를 리스트에 더함
        # print(totalscr_list)

    k_scr = totalscr_list[k - 1] #k번째 학생의 점수를 변수에 저장
    totalscr_list.sort(reverse=True) #전체 점수를 내림차순으로 정렬함
    proportion = int(N / 10) #학점 별 비율 변수 지정
    degree = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0'] #학점 리스트

    is_while_over = False
    while k_scr in totalscr_list: #k의 점수가 전체 리스트에 존재하는 조건에서
        if is_while_over == True:
            break

        for i in range(len(degree)): #각 학점에 대해 반복
            if k_scr in totalscr_list[:proportion]: #k의 점수가 전체 리스트 중 최대 성적의 비율 안에 있으면

                print(f'#{tc} {degree[i]}') #테스트케이스 회차와 학점의 종류를 출력
                is_while_over = True
                break #출력했으면 조건문 끝냄
            else:
                totalscr_list = totalscr_list[proportion:] #k의 점수가 비율 안에 없으면, 전체 리스트에서 해당 비율의 부분을 제외함
            # print(totalscr_list, proportion, totalscr_list[proportion:])
