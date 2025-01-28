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
