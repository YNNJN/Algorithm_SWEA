#직사각형 세 변의 길이가 주어짐
#나머지 한 변의 길이를 출력
t = int(input())
for tc in range(1, t+1):
    side = list(map(int, input().split()))
    l = []
    for ele in side:
        if ele in l:
            l.remove(ele)
        else:
            l.append(ele)
    print('#{} {}'.format(tc, ''.join(map(str, l))))
