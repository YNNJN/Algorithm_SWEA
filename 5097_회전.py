#맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 할 때 수열의 맨 앞에 있는 숫자를 출력
for tc in range(int(input())):
    n,m = map(int, input().split())
    nums = list(map(int, input().split()))
    while m > 0:
        x = nums.pop(0)
        nums.append(x)
        m -= 1
    print('#{} {}'.format(tc+1, nums[0]))