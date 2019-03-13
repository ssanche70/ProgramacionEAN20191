from unittest import TestCase
import Semana_5.ejemplos_if_2 as f

class TestCuadrado_primero(TestCase):
    def test_cuadrado_primero(self):
        self.assertEquals(f.cuadrado_primero(2,4),'Segundo cuadrado del primero')
        self.assertEquals(f.cuadrado_primero(2, 3), 'Segundo es menor al cuadrado del primero')
        self.assertEquals(f.cuadrado_primero(2, 5), 'Segundo es mayor al cuadrado del primero')
        self.assertEquals(f.cuadrado_primero(2, 3), 'Segundo es menor al cuadrado del primero')
        self.assertRaises(TypeError)