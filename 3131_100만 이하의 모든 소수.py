n = 10**6
a = [0,0] + [1]*(n-1)
primes = []
for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(i, n+1, i):
            a[j] = 0
for i in range(len(primes)):
    print(primes[i], end=' ')
