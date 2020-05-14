for tc in range(int(input())):
    n,m = map(int, input().split())
    arr1 = sorted(list(map(int, input().split())))
    arr2 = list(map(int, input().split()))

    cnt = 0
    for ele in arr2:
        s,e = 0, n-1

        flag = -1
        while s <= e:
            mid = (s + e) // 2
            if ele >= arr1[mid]:
                if ele == arr1[mid]:
                    cnt += 1
                    break
                s = mid + 1
                if flag == 1: break
                flag = 1

            else:
                e = mid - 1
                if flag == 0: break
                flag = 0

    print('#{} {}'.format(tc+1, cnt))


# binarySearch 구현
# def binarySearch(a, key):
#     s,e = 0, len(a) - 1
#     while s <= e:
#         mid = (s+e) // 2
#         if a[mid] == key:
#             return True
#         elif a[mid] > key:
#             e = mid - 1
#         else:
#             s = mid + 1
#     return False



