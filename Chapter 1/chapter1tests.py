import unittest

from chapter1 import *


class Chapter1Tests(unittest.TestCase):
    def test_isUnique(self):
        self.assertTrue(isUnique("abcdefg"))
        self.assertFalse(isUnique("abcbdefg"))

    def test_checkPerm(self):
        self.assertTrue(checkPerm("abcd", "adcb"))
        self.assertTrue(checkPerm("abbccd", "dcbcba"))
        self.assertFalse(checkPerm("aabbcc", "abbacb"))

    def test_urlify(self):
        self.assertEqual(urlify("test ing urlify", 15), "test%20ing%20urlify")
        self.assertEqual(urlify("test  ing again      ", 15), "test%20%20ing%20again")

    def test_isPalindromePermutation(self):
        self.assertTrue(isPalindromePermutation("hannah"))
        self.assertTrue(isPalindromePermutation("nahnah"))
        self.assertTrue(isPalindromePermutation("aahhnn"))
        self.assertTrue(isPalindromePermutation("nanahh"))
        self.assertFalse(isPalindromePermutation("nnnaah"))

    def test_oneAway(self):
        self.assertTrue(oneAway("pale", "ple"))
        self.assertTrue(oneAway("pales", "pale"))
        self.assertTrue(oneAway("pale", "bale"))
        self.assertFalse(oneAway("pale", "bake"))

    def test_stringComp(self):
        self.assertEqual(stringComp("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(stringComp("bb"), "bb")
        self.assertEqual(stringComp("a"), "a")
        self.assertEqual(stringComp("abcd"), "abcd")

    def test_rotateMatrix(self):
        self.assertEqual(rotateMatrix([['a', 'b', 'c'],
                                       ['d', 'e', 'f'],
                                       ['g', 'h', 'i']]),
                         [['g', 'd', 'a'],
                          ['h', 'e', 'b'],
                          ['i', 'f', 'c']])

    def test_zeroMatrix(self):
        matrix = [[1, 2, 3],
                  [4, 0, 6],
                  [7, 8, 0]]
        zeroMatrix(matrix)
        self.assertEqual(matrix, [[1, 0, 0],
                                  [0, 0, 0],
                                  [0, 0, 0]])

    def test_stringRotation(self):
        s1 = "waterbottle"
        s2 = "erbottlewat"
        self.assertTrue(stringRotation(s1, s2))
        self.assertTrue(stringRotation(s2, s1))

if __name__ == '__main__':
    unittest.main()
