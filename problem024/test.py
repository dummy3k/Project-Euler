import unittest

try:
    import euler_tools
except ImportError:
    print "Hacked!"
    import sys, os
    sys.path.append( os.path.join( os.getcwd(), '..' ) )

from euler_tools.permutation import next_number


class TestProblem(unittest.TestCase):
    def testResult(self):
        current = map(lambda x: int(x), str("0123456789"))
        for n in range(1000000 - 1):
            current = next_number(current)

        as_number = reduce(lambda r, x: r * 10 + x, current)
        self.assertEqual(as_number, 2783915460)

if __name__ == '__main__':
    unittest.main()
