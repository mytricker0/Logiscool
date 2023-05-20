matrix = [[4, 23, 8], [2], [63, 4, 15, 16], [4, 7]]
max_len = 0
for row in matrix:
    for item in row:
        print(item, end=" ")
    print("")
for i in matrix:
    if len(i) > max_len:
        max_len = len(i)
for j in matrix:
    k = max_len - len(j)
    while k > 0:
        j.append(0)
        k -= 1
for row in matrix:
    for item in row:
        print(item, end=" ")
    print("")