t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lab = [list(map(int, input().split())) for _ in range(n)]
    info = []
    for i in range(n):
        for j in range(n):
            garo, sero = 0,0
            if lab[i][j] != 0:
                garo += 1
                sero += 1
                k = 1
                while j+k < n:
                    if lab[i][j+k] != 0:
                        garo += 1
                        k += 1
                    else:
                        break
                p = 1
                while i+p < n:
                    if lab[i+p][j] != 0:
                        sero += 1
                        p += 1
                    else:
                        break
                info.append([sero, garo, sero*garo])
                for q in range(i,i+p):
                    for qq in range(j,j+k):
                        lab[q][qq] = 0
    #key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬함
    l = sorted(info, key = lambda x: (x[2], x[0]))
    for li in range(len(l)):
        del l[li][2]
    print('#{}'.format(tc), end=' ')
    print(len(l), end=' ')
    l2 = []
    for ele in range(len(l)):
        for el in range(2):
            l2.append(l[ele][el])
    print(' '.join(map(str, l2)))