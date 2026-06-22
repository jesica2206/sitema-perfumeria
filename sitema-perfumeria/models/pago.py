class Pago:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS pago (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_pedido INTEGER NOT NULL,
                monto REAL NOT NULL,
                metodo_pago TEXT NOT NULL,
                estado TEXT NOT NULL,
                FOREIGN KEY (id_pedido) REFERENCES pedido(id)
            )
        ''')
        self.conn.commit()

    def registrar(self, id_pedido, monto, metodo_pago, estado):
        self.cursor.execute('''
            INSERT INTO pago (id_pedido, monto, metodo_pago, estado) VALUES (?, ?, ?, ?)
        ''', (id_pedido, monto, metodo_pago, estado))
        self.conn.commit()
        return self.cursor.lastrowid

    def obtener_por_pedido(self, id_pedido):
        self.cursor.execute('SELECT * FROM pago WHERE id_pedido = ?', (id_pedido,))
        return self.cursor.fetchone()