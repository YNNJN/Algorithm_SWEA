#덱을 퍼펙트 셔플한 결과를 한 줄에 카드 이름을 공백으로 구분하여 출력
def shuffle(n):
    if n % 2 == 0:
        l = []
        for i in range(n//2):
            l.append(card[:n//2][i])
            l.append(card[n//2:][i])
        return l
    else:
        l2 = []
        for i in range(n//2):
            l2.append(card[:n//2+1][i])
            l2.append(card[n//2+1:][i])
        l2.append(card[:n//2+1][n//2])
        return l2

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    card = list(input().split())
    print('#{} {}'.format(tc, ' '.join(map(str, shuffle(n)))))