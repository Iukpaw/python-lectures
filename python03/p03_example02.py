
even = 0
odd = 0

for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Total even numbers: {even}")
print(f"Total odd numbers: {odd}")

