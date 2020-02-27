
t = int(input())

for tc in range(1, t+1):
    N = input()

    pre_row=[1]
    print(1)
    for row in range(1,int(N)):
        post_row = [ele for ele in pre_row] # 이전 행을 복사 :  바로 위에서 덧셈

        post_row.append(0)

        for i in range(len(pre_row)):
            post_row[i+1]+= pre_row[i] #이전 칸의 덧셈

        pre_row=post_row #새로운 칸

        [print(ele,end=' ') for ele in post_row[:-1]]
        print(post_row[-1])




#실행시간 0.14438s