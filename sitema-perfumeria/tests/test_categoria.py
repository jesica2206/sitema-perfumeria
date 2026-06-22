import unittest
import sqlite3
from models.categoria import Categoria

class TestCategoria(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.model = Categoria(self.conn)

    def test_crear_categoria(self):
        id_cat = self.model.crear("Amaderados", "Perfumes con notas de madera")
        self.assertIsNotNone(id_cat)
        cat = self.model.obtener(id_cat)
        self.assertEqual(cat[1], "Amaderados")

    def tearDown(self):
        self.conn.close()