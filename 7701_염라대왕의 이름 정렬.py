#이름 길이가 짧을수록, 같은 길이면 사전 순으로 앞에, 같은 이름은 하나만
for tc in range(int(input())):
    n = int(input())
    names = set()
    for i in range(n):
        names.add(input())
    names = sorted(names) # names.sort(key = lambda x: (len(x), x))
    names.sort(key = len)
    print('#{}'.format(tc+1))
    for name in names:
        print(name)



