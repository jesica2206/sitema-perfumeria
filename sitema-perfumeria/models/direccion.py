class Direccion:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS direccion (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL,
                calle TEXT NOT NULL,
                ciudad TEXT NOT NULL,
                provincia TEXT NOT NULL,
                es_principal INTEGER DEFAULT 0,
                FOREIGN KEY (id_usuario) REFERENCES usuario(id)
            )
        ''')
        self.conn.commit()

    def crear(self, id_usuario, calle, ciudad, provincia, es_principal=0):
        self.cursor.execute('''
            INSERT INTO direccion (id_usuario, calle, ciudad, provincia, es_principal)
            VALUES (?, ?, ?, ?, ?)
        ''', (id_usuario, calle, ciudad, provincia, es_principal))
        self.conn.commit()
        return self.cursor.lastrowid

    def obtener_por_usuario(self, id_usuario):
        self.cursor.execute('SELECT * FROM direccion WHERE id_usuario = ?', (id_usuario,))
        return self.cursor.fetchall()