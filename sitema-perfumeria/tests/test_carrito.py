import unittest
import sqlite3
from models.usuario import Usuario
from models.carrito import Carrito

class TestCarrito(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.user_model = Usuario(self.conn)
        self.model = Carrito(self.conn)
        self.id_user = self.user_model.crear("Sofi", "sofi@test.com", "hash", "1998-05-05")

    def test_crear_carrito_unico(self):
        id_car = self.model.crear(self.id_user)
        self.assertIsNotNone(id_car)
        id_car_repetido = self.model.crear(self.id_user)
        self.assertIsNull = id_car_repetido is None

    def tearDown(self):
        self.conn.close()