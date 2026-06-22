import unittest
import sqlite3
from models.usuario import Usuario

class TestUsuario(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.model = Usuario(self.conn)

    def test_crear_y_obtener_usuario(self):
        id_user = self.model.crear("Cris", "cris@test.com", "hash123", "1995-01-01")
        self.assertIsNotNone(id_user)
        user = self.model.obtener(id_user)
        self.assertEqual(user[1], "Cris")
        self.assertEqual(user[2], "cris@test.com")

    def tearDown(self):
        self.conn.close()