
for i in range(1, 10):
    if i % 2 == 0:
        for j in range(1, 1000):
            if j == i ** 2:
                print(i, '*', i, '=', j)
