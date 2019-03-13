from unittest import TestCase
import Semana_5.ejemplos_if_2 as f

class TestBilletes_verdes(TestCase):
    def test_billetes_verdes(self):
        self.assertEquals(f.billetes_verdes('434'),'2 billetes de 200 1 billete de 20 euros 1 billete de 10 euros 2 monedas de 2 euros')
        self.assertEquals(f.billetes_verdes('626'),'3 billetes de 200 1 billete de 20 euros 3 monedas de 2 euros')
        self.assertEquals(f.billetes_verdes('1298'), '6 billetes de 200 4 billete de 20 euros 1 billete de 10 euros 4 monedas de 2 euros')
