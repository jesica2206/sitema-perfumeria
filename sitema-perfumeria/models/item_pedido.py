class ItemPedido:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS item_pedido (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_pedido INTEGER NOT NULL,
                id_perfume INTEGER NOT NULL,
                cantidad INTEGER NOT NULL,
                FOREIGN KEY (id_pedido) REFERENCES pedido(id),
                FOREIGN KEY (id_perfume) REFERENCES perfume(id)
            )
        ''')
        self.conn.commit()

    def agregar(self, id_pedido, id_perfume, cantidad):
        self.cursor.execute('''
            INSERT INTO item_pedido (id_pedido, id_perfume, cantidad) VALUES (?, ?, ?)
        ''', (id_pedido, id_perfume, cantidad))
        self.conn.commit()
        return self.cursor.lastrowid

    def obtener_por_pedido(self, id_pedido):
        self.cursor.execute('SELECT * FROM item_pedido WHERE id_pedido = ?', (id_pedido,))
        return self.cursor.fetchall()