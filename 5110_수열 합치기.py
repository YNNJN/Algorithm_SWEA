for tc in range(int(input())):
    n,m = map(int, input().split())
    nums = list(map(int, input().split()))
    for _ in range(m-1):
        tmp_nums = list(map(int, input().split()))
        for idx in range(len(nums)):
            if nums[idx] > tmp_nums[0]:
                nums[idx:idx] = tmp_nums
                break
        else:
            nums += tmp_nums
    print('#{} {}'.format(tc+1, ' '.join(list(map(str, nums[::-1][:10])))))
