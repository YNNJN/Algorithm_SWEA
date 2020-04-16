#m개의 숫자를 지정된 위치에 추가
#완성된 수열에서 인덱스 l의 데이터를 출력하는 프로그램을 작성

for tc in range(int(input())):
    n,m,l = map(int, input().split())
    arr = list(map(int, input().split()))

    idx = []
    for _ in range(m):
        idx += list(map(int, input().split()))
    for x in range(0, len(idx), 2):
        arr.insert(idx[x], idx[x+1])

    print('#{} {}'.format(tc+1, arr[l]))