# 이진트리의 두 정점이 명시될 때 공통 조상 중 가장 가까운 정점 찾고
# 그 정점을 루트로 하는 서브 트리의 크기 찾기

for tc in range(int(input())):
    v, e, n1, n2 = map(int, input().split())
    tree = [[0 for _ in range(3)] for _ in range(v+1)]
    edges = list(map(int, input().split()))

    for i in range(e):
        p = edges[i * 2]
        c = edges[i * 2 + 1]
        if not tree[p][0]:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p

    p1 = [n1]
    while tree[n1][2]:
        n1 = tree[n1][2]
        p1.append(n1)
    while tree[n2][2]:
        n2 = tree[n2][2]
        if n2 in p1:
            p = n2
            break

    sub = [p]
    idx = 0
    while idx < len(sub):
        l = tree[sub[idx]][0]
        r = tree[sub[idx]][1]
        if l: sub.append(l)
        if r: sub.append(r)
        idx += 1
    print('#{} {} {}'.format(tc+1, sub[0], idx))