t = int(input())

for i in range(1, t+1):
    _ = input()
    raw_scrs=input()
    scrs=[]
    while ' ' in raw_scrs:
        idx=raw_scrs.index(' ')
        scrs.append(int(raw_scrs[:idx]))
        raw_scrs=raw_scrs[idx+1:]

    cnt = [0 for j in range(101)]
    for scr in scrs:

        cnt[scr] += 1

    print(cnt)
    major = max(cnt)

    result=[j*(major==cnt[j]) for j in range(101)]
    idx_major=max(result)
    print(f'#{i} {idx_major}')