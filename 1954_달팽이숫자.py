t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [[0 for i in range(n)] for j in range(n)]
    i,j = (0,0)
    direc = ['r','d','l','u']
    direc_idx = 0

    for num in range(1,n*n+1):
        arr[i][j]=num

        current_direc = direc[direc_idx]
        if current_direc == 'r':
            if j+1 == n or arr[i][j+1] != 0 :
                direc_idx += 1
                direc_idx = direc_idx%4
                i += 1
            else :
                j += 1
        elif current_direc =='d':
            if i+1==n or arr[i+1][j]!= 0 :
                direc_idx += 1
                direc_idx = direc_idx%4
                j -= 1
            else :
                i += 1
        elif current_direc == 'l':
            if j==0 or arr[i][j-1]!=0 :
                direc_idx += 1
                direc_idx = direc_idx%4
                i -= 1
            else :
                j -= 1
        else :
            if arr[i-1][j]!=0:
                direc_idx += 1
                direc_idx = direc_idx % 4
                j += 1
            else:
                i -= 1
    #출력

        # i,j=loca
        # arr[i][j] = num

        # i,j  중 어떤걸 증가시킬지
        # 증가 시켜도 되는지?
        # -> 우 j+=1 , 하 i+=1, 좌 j-=1, 상 i-=1

    print(f'#{tc}')
    for ele in arr:
        for el in ele[:-1]:
            print(el, end = ' ')
        print(ele[-1])

    # [print(ele, end = '\n') for ele in arr]


#dfs
#for문이 꼭 정상꼴의 인덴테이션만 갖는 것은 아님
#머릿속에서 순서도 돌려보고 위치 정할 것
