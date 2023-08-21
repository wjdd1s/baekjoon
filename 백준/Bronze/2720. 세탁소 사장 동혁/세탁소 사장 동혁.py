T = int(input())

for _ in range(T):
    a = int(input())
    for i in [25, 10, 5, 1]:
        print(a//i, end = " ")
        a = a%i