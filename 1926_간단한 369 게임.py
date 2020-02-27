#num = int(input())

#for i in range(1, num):
#    three = [3, 6, 9]

#    if i in three:
#        print('-', end=' ')

#    else:
#        print(i, end=' ')

#print(num)


num = input()
n_three = ['3', '6', '9']

for j in range(1, int(num)):
    cnt = 0
    current_num = str(j)

    for i in range(len(current_num)):

        if current_num[i] in n_three:
            cnt += 1

    if cnt > 0:
        print(cnt * '-', end=' ')

    else:
        print(current_num, end=' ')

print(num)

