class Resena:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS resena (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL,
                id_perfume INTEGER NOT NULL,
                calificacion INTEGER NOT NULL,
                comentario TEXT,
                FOREIGN KEY (id_usuario) REFERENCES usuario(id),
                FOREIGN KEY (id_perfume) REFERENCES perfume(id)
            )
        ''')
        self.conn.commit()

    def crear(self, id_usuario, id_perfume, calificacion, comentario):
        self.cursor.execute('''
            INSERT INTO resena (id_usuario, id_perfume, calificacion, comentario) VALUES (?, ?, ?, ?)
        ''', (id_usuario, id_perfume, calificacion, comentario))
        self.conn.commit()
        return self.cursor.lastrowid

    def obtener_por_perfume(self, id_perfume):
        self.cursor.execute('SELECT * FROM resena WHERE id_perfume = ?', (id_perfume,))
        return self.cursor.fetchall()