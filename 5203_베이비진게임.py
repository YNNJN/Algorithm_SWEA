'''
카운트 배열 이용
triplet - 숫자의 개수를 count한 배열에 3이 있는지 확인
run - 숫자의 개수를 count한 배열 중 0 이상 값의 인덱스를 뽑아
    한 칸 떨어진 인덱스의 차이가 2인지 확인

'''


def is_run(arr):
    return True if 3 in arr else False

def is_triplet(arr):
    card = [i for i in range(len(arr)) if arr[i] > 0]
    for i in range(2, len(card)):
        if card[i] - card[i-2] == 2:
            return True
    return False

def whois_winner(p1, p2):
    if (is_triplet(p1) or is_run(p1)) and (not is_triplet(p2) and not is_run(p2)):
        return 1
    elif (is_triplet(p2) or is_run(p2)) and (not is_triplet(p1) and not is_run(p1)):
        return 2
    else:
        return 0

for tc in range(int(input())):
    arr = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    winner = 0
    for i in range(len(arr)):
        if i >= 6:
            winner = whois_winner(p1, p2)
            if winner:
                break
        if i % 2:
            p2[arr[i]] += 1
        else:
            p1[arr[i]] += 1
    print(p1, p2)
    winner = whois_winner(p1, p2)
    print('#{} {}'.format(tc+1, winner))


    # p1 = [arr[i] for i in range(len(arr)) if i % 2 == 0]
    # p2 = [arr[i] for i in range(len(arr)) if i % 2 == 1]

