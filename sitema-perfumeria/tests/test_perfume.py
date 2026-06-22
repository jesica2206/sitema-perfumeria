import unittest
import sqlite3
from models.categoria import Categoria
from models.perfume import Perfume

class TestPerfume(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.cat_model = Categoria(self.conn)
        self.model = Perfume(self.conn)
        self.id_cat = self.cat_model.crear("Citricos", "Notas frescas")

    def test_crear_perfume(self):
        id_perfume = self.model.crear(self.id_cat, "One", "CK", "Cítrica", "EDT", 45000.0, 10, "Clásico")
        self.assertIsNotNone(id_perfume)
        perfume = self.model.obtener(id_perfume)
        self.assertEqual(perfume[2], "One")

    def tearDown(self):
        self.conn.close()