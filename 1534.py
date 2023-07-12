for i in range(2, 10, 2):
    for j in range(1, 10, 1):
        print(i * j)


for i in range(2, 10, 2):
    for j in range(1, 10, 1):
        print(f"{i}x{j}={i*j}")

for i in range(1, 10):
    if i % 2 == 0:
        for j in range(1, 10):
            print(f"{i}x{j}={i*j}")
