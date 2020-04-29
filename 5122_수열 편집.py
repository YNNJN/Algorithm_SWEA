for tc in range(int(input())):
    n,m,l = map(int, input().split())
    nums = list(map(int, input().split()))
    for _ in range(m):
        info = list(input().split())
        if info[0] == 'I':
            nums.insert(int(info[1]), int(info[2]))
        elif info[0] == 'D':
            nums = nums[:int(info[1])] + nums[int(info[1])+1:]
        else:
            nums[int(info[1])] = int(info[2])
    if len(nums) >= l:
        print('#{} {}'.format(tc+1, nums[l]))
    else:
        print('#{} {}'.format(tc+1, -1))