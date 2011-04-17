import datetime

def is_palindrome(x):
    x_str = str(x)
    for n in range(len(x_str) / 2):
        if x_str[n] != x_str[len(x_str) - n - 1]:
            return False

    return True

do_debug = True
def ipython():
    """ break and jump into ipython. call it this way:
            h.debug()('foo')
    """

    if not do_debug:
        def noop():
            pass
        return noop

    from IPython.Shell import IPShellEmbed
    # '-pdb',
    args = ['-pi1', 'In <\\#>: ', '-pi2', '   .\\D.: ',
            '-po', 'Out<\\#>: ', '-nosep']
    ipshell = IPShellEmbed(args,
        banner = 'Entering IPython.  Press Ctrl-D to exit. Set h.do_debug=False to never go here again.',
        exit_msg = 'Leaving Interpreter, back to Pylons.')
    return ipshell

class LossyPrinter():
    def __init__(self, intervall):
        self.intervall = intervall
        self.ts = datetime.datetime.now()
        self.ts_start = datetime.datetime.now()

    def try_print(self, s):
        if (datetime.datetime.now() - self.ts).seconds > self.intervall:
            self.ts = datetime.datetime.now()
            delta = datetime.datetime.now() - self.ts_start
            print "[%02i:%02i] %s" % (delta.seconds / 60, delta.seconds % 60, s)

class StopWatch():
    def __init__(self):
        self.ts_start = datetime.datetime.now()
        self.ts_end = None

    def stop(self):
        self.ts_end = datetime.datetime.now()

    def print_time(self, msg=None):
        if not self.ts_end:
            self.stop()

        delta = self.ts_end - self.ts_start
        if msg:
            print "Runtime:  %02i:%02i (%s)" % (delta.seconds / 60, delta.seconds % 60, msg)
        else:
            print "Runtime:  %02i:%02i" % (delta.seconds / 60, delta.seconds % 60)

def fib(max=None):
    alpha = 1
    yield alpha

    beta = 1
    yield beta

    while True:
        tmp = alpha + beta
        alpha = beta
        beta = tmp
        if max and beta > max:
            return

        yield beta

def find(fn, sequence):
    for item in sequence:
        if fn(item):
            return item

    raise Exception("no match")
