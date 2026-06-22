import unittest
import sqlite3
from models.pedido import Pedido

class TestPedido(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.model = Pedido(self.conn)

    def test_crear_pedido(self):
        id_ped = self.model.crear(1, "PED-10023", 85000.0, "PENDIENTE", "TARJETA")
        self.assertIsNotNone(id_ped)
        pedido = self.model.obtener(id_ped)
        self.assertEqual(pedido[2], "PED-10023")

    def tearDown(self):
        self.conn.close()