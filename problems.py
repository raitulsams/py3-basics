def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# print(prime(4))


def palindrome(s):
    # return s == s[::-1]
    x = slice(None, None, -1)
    return s == s[x]


# print(palindrome("racecar"))
output = []


def rec_list(lst):
    for i in lst:
        if isinstance(i, list):
            rec_list(i)
            # if i is None:
            #     return
            # output.append(rec_list(i))
        else:
            # print(i)
            output.append(i)
    # print(output)

    return output


# print(rec_list([1, 2, 3, ["a", "b", "c"]]))
print(rec_list([1, 2, 3, ["a", "b", "c", ["sams", "rahim", "karim", [1, 2, [4, 5, 6], 3]]]]))
# rec_list([1, 2, 3, ["a", "b", "c", ["sams", "rahim", "karim", [1, 2, 3]]]])
