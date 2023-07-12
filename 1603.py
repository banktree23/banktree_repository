n = 5
result = 1
while n > 0:
    result *= n
    n -= 1
print(result)

while n > 0:
    result *= n
    n -= 1
    print(f"result: {result}, n: {n}")
print(result)


n = 5
result = 1
while True:
    if n == 0:
        break

    result *= n
    n -= 1
print(result)
