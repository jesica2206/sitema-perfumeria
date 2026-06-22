class Pedido:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS pedido (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL,
                numero_pedido TEXT NOT NULL,
                total REAL NOT NULL,
                estado TEXT NOT NULL,
                metodo_pago TEXT NOT NULL,
                num_seguimiento TEXT,
                FOREIGN KEY (id_usuario) REFERENCES usuario(id)
            )
        ''')
        self.conn.commit()

    def crear(self, id_usuario, numero_pedido, total, estado, metodo_pago, num_seguimiento=None):
        self.cursor.execute('''
            INSERT INTO pedido (id_usuario, numero_pedido, total, estado, metodo_pago, num_seguimiento)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (id_usuario, numero_pedido, total, estado, metodo_pago, num_seguimiento))
        self.conn.commit()
        return self.cursor.lastrowid

    def obtener(self, id_pedido):
        self.cursor.execute('SELECT * FROM pedido WHERE id = ?', (id_pedido,))
        return self.cursor.fetchone()