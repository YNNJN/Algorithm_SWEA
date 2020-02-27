def palin(word):
    if word == word[::-1]:
        return 1
    return 0

t = int(input())
for i in range(1, t+1):
    word = input()
    print(f'#{i} {palin(word)}')