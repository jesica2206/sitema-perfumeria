import unittest
import sqlite3
from models.favorito import Favorito

class TestFavorito(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.model = Favorito(self.conn)

    def test_agregar_favorito(self):
        id_fav = self.model.agregar(1, 4)
        self.assertIsNotNone(id_fav)
        favs = self.model.obtener_por_usuario(1)
        self.assertEqual(len(favs), 1)

    def tearDown(self):
        self.conn.close()