import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("hello"),"Bonjour")
        self.assertEqual(english_to_french("welcome"),"Bienvenue")
        self.assertEqual(english_to_french("love"),"Amour")
        #self.assertEqual(english_to_french(""),"error")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertEqual(french_to_english("Bienvenue"),"welcome")
        self.assertEqual(french_to_english("Amour"),"love")

unittest.main()