bank = int(input("Enter amount of deposit: "))
years = int(input("Enter years of deposit: "))

for _ in range(years):
    bank = bank * 10

print("Final amount of deposit: ", bank)