# Author: Marcela Silverio
#****************************************************************************
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#****************************************************************************

soma = 0

for numero in range(1000):

    if numero % 3 == 0 or numero % 5 == 0:

        soma += numero

print (soma)