for tc in range(int(input())):
    n, m, k = map(int, input().split())
    nums = list(map(int, input().split()))

    idx = 0
    for _ in range(1, k + 1):
        idx += m
        if idx < n:
            nums.insert(idx, nums[idx - 1] + nums[idx])
        else:
            if idx % n:
                idx %= n
                nums.insert(idx, nums[idx - 1] + nums[idx])
            else:
                nums.insert(idx, nums[-1] + nums[0])
        n += 1

    print('#{} {}'.format(tc+1, ' '.join(list(map(str, nums[::-1][:10])))))
