#1933. 간단한 N의 약수
a=int(input())
l=[]
for i in range(a,-1,-1):
    l.append(str(i))
print(' '.join(l))
