def reverse_integer(value):
    if value < 10:
        return value
    else:
        integer_reversed = str(value%10) + str(reverse_integer(value//10))
        return integer_reversed
