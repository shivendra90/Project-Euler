# Calculates the difference of sum of squares of natural numbers
# and square of the sum of thosevery same numbers.

n = 100  # You can always change this setting
sum_of_squares = 0
square_of_sums = 0
all_sums = 0

for (number in 1:n) {
    sum_of_squares <- sum_of_squares + number^2
    all_sums <- all_sums + number
    number <- number + 1
    square_of_sums <- all_sums^2
}
print(sum_of_squares)
print(all_sums)
print(square_of_sums)

print(paste("The difference between sum of squares and square of sums of the first hundred natural numbers is", square_of_sums - sum_of_squares))
