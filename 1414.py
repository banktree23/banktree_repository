num_of_patients = int(input("Enter: "))
if num_of_patients % 3 == 0:
    print(f"{num_of_patients}은 3의 배수")
elif num_of_patients % 7 == 0:
    print(f"{num_of_patients}은 7의 배수")
elif num_of_patients % 3 == 0 or num_of_patients % 7 == 0:
    print(f"{num_of_patients}은 3의 배수, 7의 배수")
else:
    print(f"{num_of_patients}은 3의 배수, 7의 배수가 아님")

# 21이 3, 7의 배수로 나오도록 하려면 순서 바꾸면 됨.
# 3의 배수 조건 충족으로 끝나버림

num_of_patients = int(input("Enter: "))
if num_of_patients % 3 == 0 or num_of_patients % 7 == 0:
    print(f"{num_of_patients}은 3의 배수, 7의 배수")
elif num_of_patients % 7 == 0:
    print(f"{num_of_patients}은 7의 배수")
elif num_of_patients % 3 == 0:
    print(f"{num_of_patients}은 3의 배수")
else:
    print(f"{num_of_patients}은 3의 배수, 7의 배수가 아님")


num_of_patients = int(input("Enter: "))
if num_of_patients % 3 == 0:
    if num_of_patients % 7 == 0:
        print(f"{num_of_patients}은 3의 배수, 7의 배수")
    elif num_of_patients % 3 == 0:
        print(f"{num_of_patients}은 3의 배수")
    elif num_of_patients % 7 == 0:
        print(f"{num_of_patients}은 7의 배수")
else:
    print(f"{num_of_patients}은 3의 배수, 7의 배수 아님")
