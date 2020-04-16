#Tree
#n을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램
def totalnode(v):
    if v == 0: return
    global node
    node += 1
    totalnode(l[v])
    totalnode(r[v])

for tc in range(int(input())):
    e,n = map(int, input().split())
    v = e+1

    arr = list(map(int, input().split()))
    l = [0] * (v+1)
    r = [0] * (v+1)

    for i in range(0, e*2, 2):
        u,v = arr[i], arr[i+1]
        if l[u] == 0:
            l[u] = v
        else:
            r[u] = v

    node = 0
    totalnode(n)

    print('#{} {}'.format(tc+1, node))

