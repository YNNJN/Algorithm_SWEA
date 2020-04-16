#Tree
for tc in range(int(input())):
    n,m,l = map(int, input().split())
    node = [0 for _ in range(n+1)]

    for _ in range(m):
        n,v = map(int, input().split())
        node[n] = v

    if len(node) % 2:
        node.append(0)

    for i in range(len(node)-1, 1, -2):
        node[i//2] = node[i] + node[i-1]

    print('#{} {}'.format(tc+1, node[l]))