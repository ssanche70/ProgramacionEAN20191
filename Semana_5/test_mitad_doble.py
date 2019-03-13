from unittest import TestCase
import Semana_5.ejemplos_if_2 as f

class TestMitad_doble(TestCase):
    def test_mitad_doble(self):
        self.assertEquals(f.mitad_doble(7,14),'Si es el doble de un impar')
        self.assertEquals(f.mitad_doble(7, 15), 'No es el doble de un impar')
        self.assertRaises(TypeError)
