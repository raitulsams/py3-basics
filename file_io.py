# The argument mode points to a string beginning with one of the following
# sequences (Additional characters may follow these sequences.):
#
# ``r''   Open text file for reading.  The stream is positioned at the
#         beginning of the file.
#
# ``r+''  Open for reading and writing.  The stream is positioned at the
#         beginning of the file.
#
# ``w''   Truncate file to zero length or create text file for writing.
#         The stream is positioned at the beginning of the file.
#
# ``w+''  Open for reading and writing.  The file is created if it does not
#         exist, otherwise it is truncated.  The stream is positioned at
#         the beginning of the file.
#
# ``a''   Open for writing.  The file is created if it does not exist.  The
#         stream is positioned at the end of the file.  Subsequent writes
#         to the file will always end up at the then current end of file,
#         irrespective of any intervening fseek(3) or similar.
#
# ``a+''  Open for reading and writing.  The file is created if it does not
#         exist.  The stream is positioned at the end of the file.  Subse-
#         quent writes to the file will always end up at the then current
#         end of file, irrespective of any intervening fseek(3) or similar.

def file_r():
    f = open("demo.txt", "r")
    print(f.read())
    f.close()


# file_r()

# Overwrite the whole txt file
def file_w():
    f = open("demo.txt", "w")
    f.write("Hello this is python knocking at the door")
    f.close()


# file_w()


def file_a():
    f = open("demo.txt", "a")
    f.write("\nAppend to the file")
    f.close()


# file_a()


# write method normally overwrite the string one by one (Not whole like the "w" mode) in the text file
def file_rw():
    f = open("demo.txt", "r+")
    # print("Existing file contains:", f.read())
    f.write("Again, This is me and only me. Hehe this is all overwritten\nHow crazy is that?")
    f.close()
    f1 = open("demo.txt", "r")
    print(f1.read())


# file_rw()


def file_rnw():
    f = open("demo.txt", "w+")
    f.write("This is my first file with w+ mode")
    f.close()


# file_rnw()


def file_rna():
    f = open("demo.txt", "a+")
    f.write("\nI am append :)")
    f.close()

    f1 = open("demo.txt", "r")
    print(f1.read())


# file_rna()


# With syntax in file io

def file_with_systax():
    # with open("demo.txt", "r") as f:
    #     print(f.read())

    with open("demo.txt", "r+") as input, open("outputfile.txt", "w+") as output:
        for i in input:
            print(i)
            output.write(i)


# file_with_systax

def testing_file_object():
    f = open("demo.txt")
    print(type(f))


# testing_file_object()


def file_chr_by_chr():
    # f = open("demo.txt", "r")

    # The for loop automatically reads the file line by line, stopping when there are no more lines left.
    with open("demo.txt", "r") as f:
        for i in f:
            print("Only file: ", i)

    # This code uses f.read() to read the entire content of the file as a single string.
    # The for loop then iterates over each character in the string (not line by line).
    # f.read() returns all the content of the file at once, including spaces and newlines.
    with open("demo.txt", "r") as f:
        for i in f.read():
            print("With file.read(): ", i)

    # f.read() first reads the entire content of the file as a single string (like in the second example).
    # Then, split() is called on this string. By default, split() breaks the string into a list of words, separating by any whitespace (spaces, newlines, etc.).
    # The for loop then iterates over the resulting list of words (not characters or lines).
    with open("demo.txt", "r") as f:
        for i in f.read().split():
            print("With file.read().split():", i)


# file_chr_by_chr()


def find_and_replace():
    # with open("demo.txt", "r+") as f:
    #     file = f.read()
    #     new_data = file.replace("Java", "Python")
    #     print("Reading:", new_data)
    # This shows hidden characters
    with open("demo.txt", "r+") as f:
        file = f.read()
        new_data = file.replace("Java", "Python")
        print("Reading:", repr(new_data))

    with open("demo.txt", "w+") as f1:
        f1.write(new_data)
        print("After replacing:\n", new_data)


find_and_replace()
