class ItemCarrito:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS item_carrito (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_carrito INTEGER NOT NULL,
                id_perfume INTEGER NOT NULL,
                cantidad INTEGER NOT NULL,
                FOREIGN KEY (id_carrito) REFERENCES carrito(id),
                FOREIGN KEY (id_perfume) REFERENCES perfume(id)
            )
        ''')
        self.conn.commit()

    def agregar(self, id_carrito, id_perfume, cantidad):
        self.cursor.execute('''
            INSERT INTO item_carrito (id_carrito, id_perfume, cantidad) VALUES (?, ?, ?)
        ''', (id_carrito, id_perfume, cantidad))
        self.conn.commit()
        return self.cursor.lastrowid

    def obtener_por_carrito(self, id_carrito):
        self.cursor.execute('SELECT * FROM item_carrito WHERE id_carrito = ?', (id_carrito,))
        return self.cursor.fetchall()