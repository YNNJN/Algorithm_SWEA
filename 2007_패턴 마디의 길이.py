t = int(input())

for tc in range(1, t+1):
    words = input()

    for len_node in range(1, 11):
        if words[:len_node] == words[len_node:(2*len_node)]:
            node = words[:len_node]
            num = len(node)

            if node[:int(len(node) / 2)] == node[int(len(node)/2):]:
                node = node[:int(len(node)/2)]
                num = len(node)

            if node[:int(len(node) / 3)] == node[int(2*len(node) / 3):]:
                node = node[:int(len(node)/3)]
                num = len(node)

    print(f'#{tc} {len(node)}')




'''
마디의 길이를 출력하는 문제
len(words) = 30
마디의 최대 길이는 10이라고 했어
그럼 최소한 워즈에서 마디가 세 번은 나올거야
그럼 노드의 길이를 1부터 10까지 준 다음
길이를 1씩 늘려가면서 바로 다음에 오는 것들이 이전에 반복한 것들과 일치하는 지를 확인하면 되겠네

두 번씩 출력하는 것이 있어서 조건을 추가해야할 것 같아
두 번씩 출력하는 이유는 주어진 워즈 내에서 짝수 개만큼, 그리고 워즈의 완전 끝까지 마디로 끊어지기 때문
노드를 중간에서 끊은 것의 앞과 뒤가 일치한다면
그것의 반절만큼이 노드인 조건을 주면 됨

아 엑소는 세 번 반복되는구나
'''