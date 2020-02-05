#1936. 가위바위보

a, b = map(int, input().split(' '))
boo=True
if a<b : boo= not boo
if {a, b} == {1, 3}: boo= not boo

print('A' if boo else 'B')



#몇 가지 케이스 분류가 필요한 지를 따지고 시작
#대각선 출력 문제 또한 적어도 i*j만큼의 출력이 있어야 하니 5*5, for문의 중첩이 필요
#먼저 가지를 짜 놓고, 나머지 세부 조건은 모듈화
#for문 여러 개 돌릴 때 반드시 고려할 것
