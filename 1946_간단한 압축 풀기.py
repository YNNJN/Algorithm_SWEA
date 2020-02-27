t = int(input())

for case in range(1, t+1):
    index = 0
    print(f'#{case}')
    tuples=[]
    for i in range(int(input())):
        alpha, num = input().split(' ')
        tuples.append((alpha,int(num)))

    for alpha,num in tuples:
        for j in range(num):
            if index < 10:
                print(alpha, end='')
                index += 1
            else:
                index = 0
                print()
                print(alpha, end='')
                index += 1
    print()
