# print("Jibon ta bedona")

def strings_():
    c = "Hello, World"
    d = c.split(",")
    print(c.split(","))
    print(type(d))

    txt = "I am \"watching\" vikings"

    print(txt)

    txt2 = "Banana is not my favorite"
    txt3 = txt2.center(200, "3")
    print(txt3)

    x = 2
    y = 5

    print(x ** y)  # same as 2*2*2*2*2

def variables():
    x, y, z = "Orange", "Mango", "Sams"
    print(x+" "+y+" "+z)
    print(x+y+z)

def casting():
    x = int(1.2)
    y= float(12.4)
    z = str("1")
    print(x)
    print(y)
    print(z)

def boolean():
    z = True
    y = False

    t = 100
    b = 400

    if t > b:
        print("{t} is greater than {b}".format(t=t, b=b))
    if t < b:
        print("{t} is less than {b}".format(t=t, b=b))
    print(z)
    print(y)

def listType():
    a = ["jibon" , "banana", "bedona"]
    print(a)

def tupleType():
    a = ("jibon" , "banana", "bedona")
    print(a)

def rangeType():
    a = range(10)
    b = range(3, 18, 2)
    print(a)
    print(b)
    for i in range(2, 8, 2):
        print("Inside loop: ", i)

    for j in range(2, 5):
        print("Pg loop: ", j)

    for k in range(12, 5, -2):
        print("Ng loop: ", k)
rangeType()