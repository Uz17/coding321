def print_character_diamond(n):
    for i in range(n):
        line = ""
        for j in range(n):
            if j < n - i:
                line += chr(65 + j)
            else:
                line += " "
        for j in range(n - 2, -1, -1):
            if j < n - i:
                line += chr(65 + j)
            else:
                line += " "
        print(line)

    for i in range(n - 1, -1, -1):
        line = ""
        for j in range(n):
            if j < n - i:
                line += chr(65 + j)
            else:
                line += " "
        for j in range(n - 2, -1, -1):
            if j < n - i:
                line += chr(65 + j)
            else:
                line += " "
        print(line)


n = int(input("Enter Digits:"))
print_character_diamond(n)
