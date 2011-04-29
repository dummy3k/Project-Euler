def kgv(a, b):
    """
        kleinstes gemeinsames vielfaches
    """
    return abs(a * b) / ggt(a, b)

def ggt(a, b):
    """
        groesster gemeinsamer teiler
    """
    while b != 0:
        h = a % b
        a = b
        b = h
    return a
