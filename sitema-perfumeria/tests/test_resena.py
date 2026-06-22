import unittest
import sqlite3
from models.resena import Resena

class TestResena(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.model = Resena(self.conn)

    def test_crear_resena(self):
        id_res = self.model.crear(1, 2, 5, "Increíble persistencia en piel")
        self.assertIsNotNone(id_res)
        resenas = self.model.obtener_por_perfume(2)
        self.assertEqual(len(resenas), 1)

    def tearDown(self):
        self.conn.close()