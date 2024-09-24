from functools import reduce

# 1. Lambda function that adds 10 to the number passed in as an argument
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15
print("# Output: 15")


# 2. Sorting a list of tuples based on the second element
data = [(1, 2), (5, 1), (3, 4), (6, 3)]
data.sort(key=lambda x: x[1])
print(data)  # Output: [(5, 1), (1, 2), (6, 3), (3, 4)]
print("# Output: [(5, 1), (1, 2), (6, 3), (3, 4)]")


# 3. Filtering a list of integers to return only the even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
print("# Output: [2, 4, 6, 8, 10]")


# 4. Using map to square each element of a list of integers
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
print("# Output: [1, 4, 9, 16, 25]")


# 5. Using reduce to calculate the sum of a list of integers
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15
print("# Output: 15")


# Optional Challenge
data = [
    (1, 2),
    (5, 1),
    (3, 4),
    (6, 3),
    (2, 5),
    (4, 6),
    (7, 8),
    (9, 7),
    (8, 9),
    (10, 10),
    (11, 12),
]

# 6. Filtering tuples where the sum of the elements is greater than 10
filtered_data = list(filter(lambda x: x[0] + x[1] > 10, data))
print(filtered_data)  # Output: [(7, 8), (9, 7), (8, 9), (10, 10), (11, 12)]
print("# Output: [(7, 8), (9, 7), (8, 9), (10, 10), (11, 12)]")


# 7. Sorting the filtered list by the second element of the tuple
filtered_data.sort(key=lambda x: x[1])
print(filtered_data)  # Output: [(9, 7), (7, 8), (8, 9), (10, 10), (11, 12)]
print("# Output: [(9, 7), (7, 8), (8, 9), (10, 10), (11, 12)]")


# 8. Reducing the filtered list to calculate the product of the first elements of the tuples
product_of_first_elements = reduce(lambda x, y: x * y, [t[0] for t in filtered_data])
print(product_of_first_elements)  # Output: 55440
print("# Output: 55440")
