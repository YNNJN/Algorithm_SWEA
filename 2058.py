#2058. 자릿수 더하기
#하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성


num = int(input())

def sum_each(num):
    result = 0
    for i in str(num):
        result += int(i)
    return result

print(sum_each(num))


