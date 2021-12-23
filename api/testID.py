from django.test import TestCase
import unittest
from views import buscarID


class testBuscaID(unittest.TestCase):
    def testeoID(self):
        self.assertEqual(buscarID(9999),"ZZZZ999")



if __name__ == "__main__":
    unittest.main()