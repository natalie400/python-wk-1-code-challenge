def two_positive(a, b, c):
    # Count the number of positive numbers using a list comprehension
    positive_count_num = sum(1 for num in (a, b, c) if num > 0)

    # Check if exactly two of the three integers are positive
    return positive_count_num == 2
print (two_positive(1, -1, -1)) 