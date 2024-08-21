def square_numbers(numbers):
    return [number ** 2 for number in numbers]

numbers = [1, 2, 3, 4, 5]
squared_numbers = square_numbers(numbers)
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
