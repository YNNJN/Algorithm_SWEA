#2063. 중간값 찾기
#전체의 중앙에 위치하는 수치 찾기. 입력으로 n개 정수 주어지고, 중간값 출력

n = int(input())

if n % 2:
    l = map(int, input().split(' '))
    l = list(l)
    result = sorted(l)
    print(result[int(len(l)/2)])