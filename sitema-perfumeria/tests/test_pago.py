import unittest
import sqlite3
from models.pago import Pago

class TestPago(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.model = Pago(self.conn)

    def test_registrar_pago(self):
        id_pago = self.model.registrar(1, 45000.0, "MERCADOPAGO", "APROBADO")
        self.assertIsNotNone(id_pago)
        pago = self.model.obtener_por_pedido(1)
        self.assertEqual(pago[3], "MERCADOPAGO")

    def tearDown(self):
        self.conn.close()