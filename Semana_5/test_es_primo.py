from unittest import TestCase
import Semana_5.ejemplos_if_2 as f

class TestEs_primo(TestCase):
    def test_es_primo(self):
        self.assertEquals(f.es_primo(8),'No es primo')
        self.assertEquals(f.es_primo(3), 'Es primo')
        self.assertRaises(TypeError)