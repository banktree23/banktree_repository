A, B = input().split()
A = int(A)
B = int(B)

if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")


A, B = list(map(int, input().split()))
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")
