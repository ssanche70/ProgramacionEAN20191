from unittest import TestCase
import Semana_5.ejemplos_if_2 as f

class TestPar_impar(TestCase):
    def test_par_impar(self):
        self.assertEquals(f.par_impar(6),'Es par')
        self.assertEquals(f.par_impar(7), 'Es impar')
        self.assertRaises(TypeError)
