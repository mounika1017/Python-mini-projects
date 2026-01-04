n = int(input("Enter number of rows: "))
oldRow = [1]
for row in range(n):
    print(" " * (n - row - 1), end="")
    for num in oldRow:
        print(num, end=" ")
    print()
    newRow = [1]
    for i in range(len(oldRow) - 1):
        newRow.append(oldRow[i] + oldRow[i + 1])
    newRow.append(1)
    oldRow = newRow
