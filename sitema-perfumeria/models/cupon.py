class Cupon:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cupon (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT NOT NULL UNIQUE,
                descuento REAL NOT NULL,
                activo INTEGER DEFAULT 1
            )
        ''')
        self.conn.commit()

    def crear(self, codigo, descuento):
        try:
            self.cursor.execute('INSERT INTO cupon (codigo, descuento) VALUES (?, ?)', (codigo, descuento))
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception:
            return None

    def buscar(self, codigo):
        self.cursor.execute('SELECT * FROM cupon WHERE codigo = ?', (codigo,))
        return self.cursor.fetchone()