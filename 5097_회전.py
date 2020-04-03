# #맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 할 때 수열의 맨 앞에 있는 숫자를 출력
# for tc in range(int(input())):
#     n,m = map(int, input().split())
#     nums = list(map(int, input().split()))
#     while m > 0:
#         x = nums.pop(0)
#         nums.append(x)
#         m -= 1
#     print('#{} {}'.format(tc+1, nums[0]))


#collections
# from collections import deque
# for tc in range(int(input())):
#     n,m = map(int, input().split())
#     a = deque(map(int, input().split()))
#     for _ in range(m):
#         a.append(a.popleft())
#     print('#{} {}'.format(tc+1, a[0]))



#원형 큐
# for tc in range(int(input())):
#     n,m = map(int, input().split())
#     front = 0
#     rear = 0
#     queue = [0] + list(map(int, input().split()))
#     rear = n
#     q_len = n + 1
#
#     for _ in range(m):
#         #dequeue()
#         front = (front + 1) % q_len
#         t = queue[front]
#         #queue[front] = 0
#         #enqueue()
#         rear = (rear + 1) % q_len
#         queue[rear] = t
#     print('#{} {}'.format(tc+1, queue[(front+1) % q_len])) #큐의 가장 첫번째는 front+1의 모드계산



#mod
for tc in range(int(input())):
    n,m = map(int, input().split())
    nums = input().split() #연산 없이 꺼내기만 하면 되니, 굳이 리스트로 받지 않아도 됨
    print('#{} {}'.format(tc+1, nums[m % n]))




