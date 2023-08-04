rest = []

for i in range(0,10):
    a = int(input())
    b = a%42
    rest += [b]
    
rest = set(rest)
print(len(rest))
