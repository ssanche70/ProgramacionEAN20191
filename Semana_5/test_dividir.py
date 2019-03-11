from unittest import TestCase
import Semana_5.ejemplos_if_2 as f

class TestDividir(TestCase):
    def test_dividir(self):
        self.assertEquals(f.dividir(6,2),3.0)
        self.assertRaises(ZeroDivisionError)
        self.assertRaises(TypeError)
