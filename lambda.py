x = lambda a: a * 3
# print(x(2))

y = lambda a, b, c: a + b + c
# print(1, 1, 1)

z = lambda a, b, c: (a + b) * c


# print(z(1, 2, 3))

def myLambdaFunc(a, b):
    return lambda c: (a * b) / c


myDouble = myLambdaFunc(2, 3)
print(myDouble(4))
