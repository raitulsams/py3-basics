# Recursive is like a loop that loop through a specific block
# Recursive function is function that call itself repeatedly
# To zone out from recursion we need to use return
# It works with the thing that is called "call stack"; it creates a layer for each call and do the task; after it gets return it tries to execute the code beneath the line the function called.
# Base case/stop condition is the code that where we decide where to stop the recursion; Like in the for/while loop there is stop condition

def recurrence(n):
    if n == 0:
        return
    print("Before calling recursion function: ", n)
    recurrence(n - 1)
    print("After calling recursion function: ", n)


# recurrence(5)


def fact(n):
    if n == 0 or n == 1:
        return 1
    return fact(n - 1) * n


# print(fact(4))

# WFA calculate the sum of first n natural numbers

def naturalsum(n):
    if n == 1:
        return 1
    return naturalsum(n - 1) + n


print(naturalsum(4))
