floor = int(input("enter the floor number :"))

if floor == 13:
    print(f"There isn't a floor {floor}")
elif floor > 13:
    print(f"Entered floor is {floor}.\nActual floor is {floor - 1}.")
else:
    print(f"Entered floor is {floor}.\nActual floor is {floor}.")
