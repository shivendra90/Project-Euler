"""
Calculates the difference of the first
hundred natural numbers' sum of the squares
of each of the number and the square of the sum
of those very same numbers.
"""

n = int(input("Please enter a number: "))
sum_of_squares = 0
all_sums = 0
square_of_sums = 0

# For example if n = 100

for number in range(1, n + 1):
    sum_of_squares += number ** 2
    all_sums += number

    square_of_sums = all_sums ** 2  # Calculates square of all_sums

print(sum_of_squares)
print(all_sums)
print(square_of_sums)

print("The difference between the sum of squares and square of sums is {}".format(square_of_sums - sum_of_squares))
