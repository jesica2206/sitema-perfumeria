import unittest
import sqlite3
from models.usuario import Usuario
from models.direccion import Direccion

class TestDireccion(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.user_model = Usuario(self.conn)
        self.model = Direccion(self.conn)
        self.id_user = self.user_model.crear("Juan", "juan@test.com", "hash", "1990-10-10")

    def test_crear_direccion(self):
        id_dir = self.model.crear(self.id_user, "Av. Corrientes 1234", "CABA", "Buenos Aires", 1)
        self.assertIsNotNone(id_dir)
        direcciones = self.model.obtener_por_usuario(self.id_user)
        self.assertEqual(len(direcciones), 1)

    def tearDown(self):
        self.conn.close()