import unittest
import sqlite3
from models.cupon import Cupon

class TestCupon(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.model = Cupon(self.conn)

    def test_cupon_descuento(self):
        self.model.crear("PERFU15", 15.0)
        cupon = self.model.buscar("PERFU15")
        self.assertIsNotNone(cupon)
        self.assertEqual(cupon[2], 15.0)

    def tearDown(self):
        self.conn.close()