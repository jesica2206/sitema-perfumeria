import unittest
import sqlite3
from models.item_pedido import ItemPedido

class TestItemPedido(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.model = ItemPedido(self.conn)

    def test_agregar_item_pedido(self):
        id_item = self.model.agregar(1, 2, 3) # Pedido=1, Perfume=2, Cantidad=3
        self.assertIsNotNone(id_item)
        items = self.model.obtener_por_pedido(1)
        self.assertEqual(len(items), 1)

    def tearDown(self):
        self.conn.close()