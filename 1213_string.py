#특정한 문자열의 개수를 반환하는 프로그램을 작성

# def bruteForce(word, words):
#     i, j, cnt = 0, 0, 0
#     for i in range(len(words)):
#         for j in range(len(word)):
#             if words[i+j] != word[j]:
#                 break
#             if j == len(word):
#                 cnt += 1
#             else:
#                 return 0
#     return cnt

def bruteForce(word, words):
    i, j, cnt = 0, 0, 0

    while j < len(word) and i < len(words):
        if words[i] != word[j]:
            i = i-j
            j = -1
        i += 1
        j += 1

        if j == len(word):
            cnt += 1
            j = 0
            i = i - len(word) + 1

    return cnt

for _ in range(1, 11):
    t = int(input())
    word = input()
    words = input()

    print(f'#{t} {bruteForce(word, words)}')