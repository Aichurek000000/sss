cup = int(input("Enter number of cups: "))
if cup % 10 == 1 and cup % 100 != 11:
    print("Чашка")
elif 2 <= cup % 10  <= 4 and 11-14 != cup:
    print("Чашки")
else:
    print("Чашек")