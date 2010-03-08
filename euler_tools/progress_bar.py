import sys
from datetime import datetime

class ProgressBar():
    def __init__(self, max):
        self.max = max
        self.value = 0
        self.last_update = None
        self.tty_width = 40

    def set_value(self, value):
        if value == self.value:
            return

        self.value == value
        if not self.last_update or (datetime.now() - self.last_update).seconds > 1:
            percent = value * 1. / self.max
            msg = "\r["
            for n in range(self.tty_width - 2):
                if float(n) / self.tty_width > percent:
                    msg += "_"
                else:
                    msg += "*"

            #~ print "\r%s" % percent,
            msg += "]"
            print msg,
            sys.stdout.flush()
            self.last_update = datetime.now()

    def clear(self):
        print "\r" + " " * self.tty_width + "\r",

    def finished(self):
        msg = "\rFinished"
        while len(msg) - 1 < self.tty_width:
            msg += " "

        print msg

