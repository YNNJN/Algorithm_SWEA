t = int(input())
for tc in range(1, t+1):
    n = int(input())
    n_list = list(map(int, input().split()))
    result = []
    even = [n_list[i] for i in range(2*n) if i % 2 == 0] #짝수번쨰의 수나사 굵기 리스트
    odd = [n_list[i] for i in range(2*n) if i % 2 == 1] #홀수번째의 암나사 굵기 리스트

    for i in range(n):
        if even[i] not in odd: #수나사 값이 암나사 리스트에 없다면 (모든 나사가 연결되어있으므로 가장 처음값)
            result.append(even[i]) #해당 암나사 값을 결과리스트에 더함
            result.append(odd[i]) #같은 인덱스의 수나사 값을 결과리스트에 더함


    while len(result) < 2*n: #전체 범위에서
        for i in range(n):
            if result[-1] == even[i]: #결과리스트의 끝 값이 수나사의 값이라면
                result.append(even[i]) #수나사의 값을 더하고
                result.append(odd[i]) #암나사의 값을 더함

    print('#{}'.format(tc), end=' ')
    [print(ele, end=' ') for ele in result[:-1]]
    print(result[-1])