def is_palindrome(x):
    x_str = str(x)
    for n in range(len(x_str) / 2):
        if x_str[n] != x_str[len(x_str) - n - 1]:
            return False

    return True


