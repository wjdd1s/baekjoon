x = [input() for _ in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(x[i]):
            print(x[i][j], end='')
