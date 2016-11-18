import unittest
from contextlib import contextmanager
import sys
from io import StringIO
from secret import *

class TestPrimes(unittest.TestCase):

    def test_primer_under200(self):
        primes_under_200 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                            97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
                            191, 193, 197, 199]
        self.assertEqual(get_primes_less_than(200), primes_under_200)


def main():
    unittest.main()

if __name__ == '__main__':
    main()