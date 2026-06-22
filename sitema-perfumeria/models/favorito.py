class Favorito:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS favorito (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL,
                id_perfume INTEGER NOT NULL,
                FOREIGN KEY (id_usuario) REFERENCES usuario(id),
                FOREIGN KEY (id_perfume) REFERENCES perfume(id)
            )
        ''')
        self.conn.commit()

    def agregar(self, id_usuario, id_perfume):
        self.cursor.execute('INSERT INTO favorito (id_usuario, id_perfume) VALUES (?, ?)', (id_usuario, id_perfume))
        self.conn.commit()
        return self.cursor.lastrowid

    def obtener_por_usuario(self, id_usuario):
        self.cursor.execute('SELECT * FROM favorito WHERE id_usuario = ?', (id_usuario,))
        return self.cursor.fetchall()