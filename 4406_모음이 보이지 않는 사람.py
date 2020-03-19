t = int(input())
for tc in range(1, t+1):
    word = list(input())
    vowel = ['a', 'e', 'i', 'o', 'u']
    for ele in vowel:
        if ele in word:
            word.remove(ele)
    print(word)
