def multiply_rec(num, num2):
    """
    This is work by adding num together once for
    each recursive call, and then ensuring the number
    of recursive calls we make is equal to num2
    :param num:
    :param num2:
    :return:
    """
    if num2 == 1:
        return num
    else:
        return num + multiply_rec(num, num2 - 1)


print(multiply_rec(5, 5))





