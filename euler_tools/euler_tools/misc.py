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
        self.ts = None

    def try_print(self, s):
        if self.ts == None:
            self.ts = datetime.datetime.now()
            print s
        elif (datetime.datetime.now() - self.ts).seconds > self.intervall:
            self.ts = datetime.datetime.now()
            print s

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

