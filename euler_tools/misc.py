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

