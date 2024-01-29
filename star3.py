rows = int(input("Enter Digits:"))

for i in range(rows):
    if i == 0 or i == rows - 1:
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))
    else:
        print(" " * (rows - i - 1) + "*" + " " * (2 * i - 1) + "*")
