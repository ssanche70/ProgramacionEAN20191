from unittest import TestCase
import Semana_5.ejemplos_if_2 as f

class TestCompara_edades(TestCase):
    def test_compara_edades(self):
        self.assertEquals(f.compara_edades(4,8),'El primero es mas joven')
        self.assertEquals(f.compara_edades(8, 4), 'El segundo es mas joven')
        self.assertEquals(f.compara_edades(4, 4), 'Tienen la misma edad')
