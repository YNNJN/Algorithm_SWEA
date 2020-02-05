#2050. 알파벳을 숫자로 변환
#알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력



alpha = input()

result = ''

for i in range(len(alpha)):
    num = ord(alpha[i])-ord('A')+1
    result += str(num) + ' '

print(result[:-1])
