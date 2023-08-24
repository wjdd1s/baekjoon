N = int(input())

room = 1
d = 1

while N>room:
    room += 6*d
    d += 1

print(d)