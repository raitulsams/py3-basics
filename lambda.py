x = lambda a: a * 3
# print(x(2))

y = lambda a, b, c: a + b + c
# print(1, 1, 1)

z = lambda a, b, c: (a + b) * c


# print(z(1, 2, 3))

def myLambdaFunc(a, b):
    return lambda c: (a * b) / c


myDouble = myLambdaFunc(2, 3)


# print(myDouble(4))

def mycustomsort():
    def myval(item):
        return item['year']

    carModel = ["BMW", "AORD", "MITSUBISHI", "VW"]
    cars = [
        {'car': 'Ford', 'year': 2005},
        {'car': 'Mitsubishi', 'year': 2000},
        {'car': 'BMW', 'year': 2019},
        {'car': 'VW', 'year': 2011}
    ]
    cars.sort(key=myval)
    carModel.sort()
    print(carModel)
    print(cars)


# mycustomsort()


def lambSort():
    # Sort a list of tuples by the second element
    data = [(10, 'b'), (2, 'a'), (3, 'c')]
    data.sort(key=lambda x: x[1])
    print(data)  # Output: [(2, 'a'), (1, 'b'), (3, 'c')]


# lambSort()


def filter_lamb():
    x = [1, 23, 4, 4, 5, 5]
    print(list(filter(lambda y: y % 2 == 0, x)))


filter_lamb()
