from unittest import TestCase
import Semana_5.ejemplos_if_2 as f

class TestEs_parentesis(TestCase):
    def test_es_parentesis(self):
        self.assertEquals(f.es_parentesis('('),'Es parentesis')
        self.assertEquals(f.es_parentesis('x'), 'No es parentesis')
        self.assertRaises(TypeError)
