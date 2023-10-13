"""
Create unit test using those cases:
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)
"""

import unittest

from exo2 import solution


class Exo2Test(unittest.TestCase):

    def fixed_tests_True(self):
        p= solution("samurai", "ai")
        solution("ninja",   "ja")
        solution("sensei",  "i")
        solution("abc",     "abc")
        solution("abcabc",  "bc")
        solution("fails",   "ails")
        self.assertEqual(True, p)