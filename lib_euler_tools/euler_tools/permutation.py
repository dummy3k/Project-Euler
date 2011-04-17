
def foo():
    return 4711

class NotFoundException(Exception):
    pass

def find(fn, sequence):
    for item in sequence:
        if fn(item):
            return item

    raise NotFoundException()

def next_number(digits):
    for pos in range(len(digits) - 2, -1, -1):
        search_window = digits[pos + 1:]
        search_value = digits[pos]
        #~ print "search_window: %s" % search_window
        #~ print "search_value: %s" % search_value

        search_window.sort()
        try:
            next_bigger = find(lambda x: x > search_value, search_window)
        except NotFoundException:
            #~ print "widening search window"
            continue

        retval = digits[:pos]
        retval.append(next_bigger)

        search_window.append(search_value)
        search_window.remove(next_bigger)
        search_window.sort()
        for item in search_window:
            retval.append(item)


        #~ print "retval: %s" % retval
        return retval



