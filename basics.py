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

def rangeList():
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
        # memory usuage of range and list
    import sys

    r = range(1, 1000000)
    print("Memory usuage of range(1, 1000000): ", sys.getsizeof(r))

    u = list(range(1, 1000000))
    print(list(range(1, 100)))
    print("list(range(1, 1000000)): ", sys.getsizeof(u))

    s = list(("jibon" , "banana", "bedona"))
    print("Memory usage of listlist((\"jibon\" , \"banana\", \"bedona\"))", sys.getsizeof(s))

    thislist = ["appel", "kola", "cherifol"]
    thislist.append("komola")
    thislist.insert(2, "komolalebu")
    print ("After inserting: ",thislist)

    listOne = list(("ami", "tumi", "ar", "danish"))
    listTwo = ["ebong", "kolagach"]
    # myList = listOne.extend(listTwo)
    listOne.extend(listTwo)
    print(listOne)
    if "komolebu" in thislist:
        print("Yes, 'komolalebu' is in the fruits list")

    listMix = list(("mera", "naam", "hain", "sikandar"))
    tupleMix = tuple(("lichu", "tokfol"))
    listMix.extend(tupleMix)
    print("After mising list and tuple datatype: ",type(listMix))
    print("Before clearing: ",listMix)
    listMix.clear()
    print("After clearing: ",listMix)
    print("After clearing the length: ",len(listMix))

# loop and if condition list


    fol = ["komol", "aam", "jambura", "goya", "ataa"]

    folerList = [x for x in fol if "a" in x]

    print("Foler namer moddhe a khujtesi: ",folerList)
    print("Foler type: ",type(folerList))

rangeList()

def sysModule():
        import sys
        print(sys.version)
        print("Platform:", sys.platform)
        print(sys.modules)
        print(sys.path)


# List: Mutable (can be modified after creation).

# You can change the values of a list, add new elements, or remove elements after it has been created.

def listDepth():
    normalList = [1, 2, 3]
    rangeInList = list(range(1, 100, 2))
    listInArray = [i for i in range(4, 8, 1)]
    print(normalList)
    print(rangeInList)
    print(listInArray)

def exploringTuple():
    tapatap = (12, 45, 67)
    print(tapatap)

exploringTuple()
