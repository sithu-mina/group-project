# Write a function to calculate the factorial of a number
# define factorial,
f = 5


def factorial(f):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    # a factorial cant be a negative number. get rid of all negative options.abs
    result = 1
    # start with a result of 1 because anything times 1 is itself.
    for i in range(2, f + 1):
        # multiply result by current number, keep adding until number given is reached to make factorial.
        result *= i
    return result
