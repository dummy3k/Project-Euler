import doctest
from euler_tools.math import ggt

def check_values(num, denom):
    """
        >>> check_values(49, 98)
        True
        >>> check_values(99, 71)
        False
    """
    for cancel in range(1, 10):
        num_str = str(num)
        denom_str = str(denom)
        if str(cancel) in num_str and str(cancel) in denom_str:
            num_str = str(num).replace(str(cancel), '')
            denom_str = str(denom).replace(str(cancel), '')
            if not num_str:
                continue
            if not denom_str or float(denom_str) == 0:
                continue

            if float(num_str) / float(denom_str) == float(num) / denom:
                #~ print "%s/%s  %s" % (num_str, denom_str, cancel)
                return True

    return False

def main():
    product_num = 1
    product_denom = 1
    for denom in range(10, 100):
        for num in range(1, denom):
            if num != denom and check_values(num, denom):
                product_num *= num
                product_denom *= denom
                print "%s/%s" % (num, denom)

    the_ggt = ggt(product_num, product_denom)
    print product_denom / the_ggt

if __name__ == '__main__':
    failed, cnt  = doctest.testmod()
    if failed == 0:
        main()
