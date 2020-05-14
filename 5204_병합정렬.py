def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(arr1, arr2):
    global cnt
    i,j = 0, 0
    result = []

    if arr1[-1] > arr2[-1]:
        cnt += 1

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result

for tc in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    print('#{} {} {}'.format(tc+1, merge_sort(arr)[n//2], cnt))



# 가독성은 더 좋지만 시간초과
# def merge(arr1, arr2):
#     global cnt
#     result = []
#     if arr1[-1] > arr2[-1]:
#         cnt += 1
#
#     while arr1 or arr2:
#         if arr1 and arr2:
#             if arr1[0] <= arr2[0]:
#                 result.append(arr1.pop(0))
#             else:
#                 result.append(arr2.pop(0))
#         elif arr1:
#             result.append(arr1.pop(0))
#         elif arr2:
#             result.append(arr2.pop(0))
#
#     return result