# 2. pyramid

n = 5
number = 1
for i in range(1, n +1):
    print("  " * (n-i), end=" ")
    for j in range(1, i*2):
        print(number, end="  ")
        number += 1
        if number > 20:
            break
    print()
