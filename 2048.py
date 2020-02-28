def transpose(arr):
    for i in range(len(arr)):
        for j in range(i):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    return arr


def reverse(arr):
    for i in range(len(arr)):
        arr[i] = arr[i][::-1]
    return arr


def left(arr, n):
    for i in range(n):
        for j in range(arr[i].count(0)):
            arr[i].append(arr[i].pop(arr[i].index(0)))
        for j in range(1, n):

            if arr[i][j - 1] == arr[i][j]:
                arr[i][j - 1] = 2 * arr[i][j - 1]
                arr[i][j] = 0
        for j in range(arr[i].count(0)):
            arr[i].append(arr[i].pop(arr[i].index(0)))
    return arr


def right(arr, n):
    reverse(arr)
    left(arr, n)
    return reverse(arr)


def up(arr, n):
    transpose(arr)
    left(arr, n)
    return transpose(arr)


def down(arr, n):
    transpose(arr)
    right(arr, n)
    return transpose(arr)


T = int(input())

for _ in range(T):
    N, S = input().split()
    N = int(N)
    nums = [list(map(int, input().split())) for i in range(N)]

    if S == 'left':
        nums = left(nums, N)
    elif S == 'right':
        nums = right(nums, N)
    elif S == 'up':
        nums = up(nums, N)
    else:
        nums = down(nums, N)

    print('#{}'.format(_ + 1))
    for i in range(N):
        print('{}'.format(" ".join(map(str, nums[i]))))