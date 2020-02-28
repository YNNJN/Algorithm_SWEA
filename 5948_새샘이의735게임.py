t = int(input())
#idxes = [(0,1,2),(0,1,3),....]

for tc in range(1, t+1):
    numbers = list(map(int, input().split()))
    s = []

    parts = []
    for i in range(1<<7):
        part = []
        for j in range(7):
            if i&(1<<j):
                part.append(numbers[j])
        parts.append(part)

    # for idx in idxes :
        # idx = (idx1, idx2, idx3)
        # s.append(sum(numbers[idx[0]],numbers[idx[1]],numbers[idx[2]]))

    for ele in parts:
        if len(ele) == 3:
            s.append(sum(ele))
    s = list(set(s))
    s = sorted(s)
    print('#{} {}'.format(tc, s[-5]))
