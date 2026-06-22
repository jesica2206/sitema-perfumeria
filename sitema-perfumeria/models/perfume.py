class Perfume:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS perfume (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_categoria INTEGER NOT NULL,
                nombre TEXT NOT NULL,
                marca TEXT NOT NULL,
                familia_olfativa TEXT,
                concentracion TEXT,
                precio REAL NOT NULL,
                stock INTEGER NOT NULL,
                descripcion TEXT,
                FOREIGN KEY (id_categoria) REFERENCES categoria(id)
            )
        ''')
        self.conn.commit()

    def crear(self, id_categoria, nombre, marca, familia_olfativa, concentracion, precio, stock, descripcion):
        self.cursor.execute('''
            INSERT INTO perfume (id_categoria, nombre, marca, familia_olfativa, concentracion, precio, stock, descripcion)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (id_categoria, nombre, marca, familia_olfativa, concentracion, precio, stock, descripcion))
        self.conn.commit()
        return self.cursor.lastrowid

    def obtener(self, id_perfume):
        self.cursor.execute('SELECT * FROM perfume WHERE id = ?', (id_perfume,))
        return self.cursor.fetchone()