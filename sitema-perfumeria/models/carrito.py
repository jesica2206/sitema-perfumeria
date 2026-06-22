class Carrito:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS carrito (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL UNIQUE,
                FOREIGN KEY (id_usuario) REFERENCES usuario(id)
            )
        ''')
        self.conn.commit()

    def crear(self, id_usuario):
        try:
            self.cursor.execute('INSERT INTO carrito (id_usuario) VALUES (?)', (id_usuario,))
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception:
            return None

    def obtener_por_usuario(self, id_usuario):
        self.cursor.execute('SELECT * FROM carrito WHERE id_usuario = ?', (id_usuario,))
        return self.cursor.fetchone()