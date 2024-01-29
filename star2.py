n = int(input("Enter Digits:"))

for i in range(n):
    if i == n - 1:
        print("*" * n)
    else:
        line = "*"
        for j in range(1, i + 1):
            if j == i:
                line += "*"
            else:
                line += " "
        print(line.ljust(n, " "))
