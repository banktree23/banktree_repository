for i in range(1, 10):
    if i % 2 != 0:
        pass
    else:
        for j in range(1, 10):
            print(f"{i}x{j}={i*j}")

# != 같지 않다
for i in range(1, 10):
    if i % 2 != 0:
        continue

    for j in range(1, 10):
        print(f"{i}x{j}={i*j}")

# pass : 그냥 지나가는 것
# continue : 조건 충족하면 과정이 종료된 후 처음으로 넘어감
#        : 조건이 충족되지 않을 시 다음으로 넘어감

for i in range(1, 10):
    print(f"##### {i}")
    if i % 2 != 0:
        break

    for j in range(1, 10):
        print(f"{i}x{j}={i*j}")
