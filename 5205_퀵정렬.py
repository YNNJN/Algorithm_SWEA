def quick_sort(arr, left, right):
    if left < right:
        pivot = lomuto_partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)

def lomuto_partition(arr, left, right):
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

for tc in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr) - 1)
    print('#{} {}'.format(tc+1, arr[n//2]))

# partition 함수2
# def hoare_partition(arr, left, right):
#     i = left
#     j = right
#     pivot = arr[left]
#
#     while i <= j:
#         while i <= j and arr[i] <= pivot:
#             i += 1
#         while i <= j and arr[j] >= pivot:
#             j -= 1

#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[left], arr[j] = arr[j], arr[left]
#
#     return j


