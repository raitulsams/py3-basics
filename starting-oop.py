# To map with real world scenarios, we started using objects in code. This is called object oriented programming

# Long ago we used procedural programming(sequentially written all code)
# Then we used functional programming where
# Using functions to reduce the redundancy and increases the reusability
# Then we came OOP
# Where we use objects and classes (it's not compulsory to use, if we need then we can)

# Real world scenario: everything is object.
# In oop we create class before creating object. Think of a classroom as Class and Students as Objects


# Class is a blueprint for creating object; Class defines what kind of features would be on the objects.
# Object is similar to the instance

# __init__ Function (Constructor)
#  All classes have a function called __init__, which is always executed when the object is being initiated.
#  It invokes when an object is created
#  __init__ always has an argument named "self". self; it's pointing to itself(the new object)
#  Constructors: Default and parameterized constructor.if we have two constructors then only the matches parameter constructor would call.
#  Attributes: class and object/instance; Class.attr, obj.attr; self.name-> object parameter; class variables are normally class variables.
#  Student and college; Student

# Classes are based on data(attributes) and methods(function)

#  Static Methods
#  Static methods are methods that do not have the self parameter; works as class level

# Abstraction
# Hiding the implementation details of a class and only showing the essential features to the user
# Think of a car starting by clicking a button. There are many mechanism happen inside the car machine but user do not look.
# Abstraction is like the clicking button and hiding the machine mechanism.


# Encapsulation
# Wrapping data and functions into a single unit(object)
# In Class, we have like constructor, static or non-static method and data attributes.
# Encapsulation is normally binding all these and whenever an object created.

class Student:
    def __init__(self, name):
        self.name = name
        print("Creating new info..")

    @staticmethod  # decorator
    def print_name():
        print("I am static method")

    name = "sams"
    age = 18


# obj = Student("sams")
# obj.print_name()
# print(obj.name)


# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.
class Account:
    def __init__(self, balance, account_no):
        self.balance = int(balance)
        self.account_no = int(account_no)

    def debit(self, amount):
        print("Debited:", amount)
        self.balance -= int(amount)

    def credit(self, amount):
        print("Credited:", amount)
        self.balance += int(amount)

    def curr_balance(self):
        print("Current Balance is", self.balance)


def get_input():
    account_no = input("Enter the account no:")
    balance = input("Enter the balance:")
    obj = Account(balance, account_no)
    debit_or_credit = input("Enter 1 for debit or 2 for credit:")
    if debit_or_credit == "1":
        obj.debit(int(input("Enter the amount:")))
        obj.curr_balance()
    elif debit_or_credit == "2":
        obj.credit(int(input("Enter the amount:")))
        obj.curr_balance()
    else:
        print("Invalid input")


get_input()
