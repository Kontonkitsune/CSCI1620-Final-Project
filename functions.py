

def simp(value) -> str:
    """
    Short for "Simplify" but funnier.
    Basically just checks if there's a simpler way to display a value.

    :param value: Usually a float,
    :return: String that's a simplified version of value
    """

    try:
        if value == int(value):
            return str(int(value))
        else:
            return str(value)
    except ValueError:
        return str(value)


def crazy_addition(a, b) -> str:
    """
    Concatenates strings

    :param a: can be a string, an int, or a float
    :param b: can be a string, an int, or a float
    :return: string of the result of the operation
    """
    return str(simp(a)) + str(simp(b))


def crazy_subtraction(a, b) -> str:
    """
    If b is a positive integer, the output is a with b characters cut off the end.
    If b is a negative integer, the output is a with b characters cut off the beginning.
    If b is zero, the output is a.
    if b is a string, all instances of b are removed from a.

    :param a: can be a string, an int, or a float
    :param b: can be a string, an int, or a float
    :return: string of the result of the operation
    """
    try:
        var1 = str(a)
        var2 = int(b)
        if abs(var2) < len(var1):
            if var2 >= 0:
                return a[:len(var1) - int(var2)]  # removes the last var2 letters
            else:
                return var1[abs(int(var2)):]  # removes the first abs(var2) letters
        else:
            return ""
    except ValueError:  # if b is also a string
        var1 = str(a)
        var2 = str(b)
        return var1.replace(var2, "")


def crazy_multiplication(a, b) -> str:
    """
    If b is an integer, the result is a repeated b times.
    If b is a float, the result is a repeated int(b) times, with a b's remainder part of a.
    If b is a string, the result is the two concatenated. (Technically correct according to algebra)

    :param a: can be a string, an int, or a float
    :param b: can be a string, an int, or a float
    :return: string of the result of the operation
    """
    try:
        var1 = str(a)
        var2 = float(b)
        if var2 == int(var2):
            return var1 * int(var2)
        else:
            return var1 * int(var2) + str(var1[0:int(len(var1) * (var2 - int(var2)))])
    except ValueError:
        return crazy_addition(a, b)


def crazy_division(a, b) -> str:
    """
    If b is an integer, the result is a slice of a with step b
    If b is a float, the result is a slice of a with step b (except occasionally skipping some)
    If b is a string, and b and a are equal, the result is one.
    If b is a string, and b is in a, the result is a with one removed instance of b.
    If b is a string, and none of the above are true, the result is Undefined.

    :param a: can be a string, an int, or a float
    :param b: can be a string, an int, or a float
    :return: string of the result of the operation
    """
    try:
        var1 = str(a)
        var2 = float(b)
        if var2 == 0:
            return "Undefined"  # cannot divide by zero
        elif var1 == str(var2):
            return "1"  # anything divided by itself is one.
        elif var2 == int(var2):
            return var1[::int(var2)]
        else:
            itvar = 0  # literal name "iteration variable"
            result = ""
            while itvar < len(var1):
                result += var1[int(itvar)]
                itvar += var2
    except ValueError:
        var1 = str(a)
        var2 = str(b)
        if var1 == str(var2):  # anything divided by itself is one.
            return "1"
        if var2 in var1:
            return var1.replace(var2, "", 1)
        else:
            return "Undefined"
