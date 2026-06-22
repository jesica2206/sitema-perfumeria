class Categoria:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS categoria (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT
            )
        ''')
        self.conn.commit()

    def crear(self, nombre, descripcion):
        self.cursor.execute('INSERT INTO categoria (nombre, descripcion) VALUES (?, ?)', (nombre, descripcion))
        self.conn.commit()
        return self.cursor.lastrowid

    def obtener(self, id_categoria):
        self.cursor.execute('SELECT * FROM categoria WHERE id = ?', (id_categoria,))
        return self.cursor.fetchone()