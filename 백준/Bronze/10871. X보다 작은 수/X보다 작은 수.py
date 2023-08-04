N, X = map(int, input().split())

for i in range(0,N):
    A = map(int, input().split())
    for p in A:
        if p<X:
            print(p, end =" ")
    break
    