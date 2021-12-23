from django.test import TestCase
import unittest
from views import buscarPatente


class testBuscaPatente(unittest.TestCase):
    def testeoPatente(self):
        self.assertEqual(buscarPatente("ZZZZ999"),9999)



if __name__ == "__main__":
    unittest.main()