import unittest
import sqlite3
from models.carrito import Carrito
from models.item_carrito import ItemCarrito

class TestItemCarrito(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.carrito_model = Carrito(self.conn)
        self.model = ItemCarrito(self.conn)
        self.id_carrito = self.carrito_model.crear(1) 

    def test_agregar_item_carrito(self):
        id_item = self.model.agregar(self.id_carrito, 5, 2) # Carrito, IdPerfume=5, Cantidad=2
        self.assertIsNotNone(id_item)
        items = self.model.obtener_por_carrito(self.id_carrito)
        self.assertEqual(len(items), 1)

    def tearDown(self):
        self.conn.close()