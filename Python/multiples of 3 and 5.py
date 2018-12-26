""" This is the calculation for the sum of all
multiples of 3 and 5 for all numbers till 1000.
"""

multiples_of_3_5 = []

for i in range(1, 1000):
    if (i) % 3 == 0 or (i) % 5 == 0:
        multiples_of_3_5.append(i)

print(multiples_of_3_5)
print(sum(multiples_of_3_5))
