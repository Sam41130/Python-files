def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = []

n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    value = int(input("Enter a number: "))
    numbers.append(value)

result = sum_numbers(numbers)

print("The sum is:", result)
