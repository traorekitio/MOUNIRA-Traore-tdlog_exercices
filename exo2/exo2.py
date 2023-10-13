"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""
def solution(chaine1, chaine2):
    taille_chaine2 = len(chaine2)
    if taille_chaine2 > len(chaine1):
        print(False)
    else:
        print(chaine2 == chaine1[-taille_chaine2:])

solution('abc', 'bc')
solution('abc', 'd')
solution('abc', 'abc')

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


class Exo2Test(unittest.TestCase):

    def fixed_tests_True(self):
        self.assertEqual(True, solution("samurai", "ai"))
        self.assertEqual(True, solution("ninja",   "ja"))
        self.assertEqual(True, solution("sensei",  "i"))
        self.assertEqual(True, solution("abc",     "abc"))
        self.assertEqual(True, solution("abcabc",  "bc"))
        self.assertEqual(True, solution("fails",   "ails"))

    def fixed_tests_False(self):
        self.assertEqual(False, solution("sumo",    "omo"))
        self.assertEqual(False, solution("samurai", "ra"))
        self.assertEqual(False, solution("abc",     "abcd"))
        self.assertEqual(False, solution("ails",    "fails"))
        self.assertEqual(False, solution("this",    "fails"))
        self.assertEqual(False, solution("spam",    "eggs"))
    