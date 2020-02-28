#n개 버스 노선, i번째 버스 노선은 번호가 a 이상 b 이하
#p개의 버스정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    num = []
    for _ in range(n):
        ab = list(map(int, input().split()))
        num.append(ab)

    p = int(input())
    c_list = []
    for _ in range(p):
        c = int(input())
        c_list.append(c)

    stop = list(0 for _ in range(p))
    for nu in num:
        for i in range(len(c_list)):
            if c_list[i] in range(nu[0],nu[1]+1):

                stop[i] += 1

    print('#{} {}'.format(tc, ' '.join(map(str,stop))))