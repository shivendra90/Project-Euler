"""
Simple calculation for finding out largest prime factor of
a  positive number.
Credit goes to Stefan: https://stackoverflow.com/a/22808285/6061080
"""


def largest_prime(x):
    """
    Finds out all the prime factors of
    a number 'x' and returns the largest
    of them.
    :param x: Integer.
    :return: maximum of list(factors).
    """
    fact = 2
    factors = []

    if x <= 1:
        return "largest prime factor for 1 is 1 itself."
    else:
        for i in range(1, x):
            if x % fact:
                fact += 1
            else:
                x //= fact
                factors.append(fact)

    message = "Largest prime factor is {}".format(max(factors))
    return message


# print(largest_prime(600851475143))

n = int(input("Please enter a number: "))
factor = 2

while n > factor:  # Factors cannot exceed n
    if n % factor:
        factor += 1
    else:
        n //= factor

print(n)
