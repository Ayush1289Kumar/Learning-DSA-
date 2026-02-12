# Print 1 to n using Recursion.

def print_1_to_n(n):
    # base case
    if n == 0:
        return

    # recursive case
    print_1_to_n(n-1)
    print(n, end=" ")


# print_1_to_n(10)
# print()

# factorial of a number.

def factorial(n):
    # base case
    if n == 0:
        return 1

    # recursive case
    return n*factorial(n-1)


# print(factorial(5))

# Fibonnaci number

def fibo(n):
    # base case
    if n == 0 or n == 1:
        return n

    # recursive case
    return fibo(n-1) + fibo(n-2)


for i in range(11):
    print(fibo(i), end=" ")
