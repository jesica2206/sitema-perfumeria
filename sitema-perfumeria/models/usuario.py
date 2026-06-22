class Usuario:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                contrasena_hash TEXT NOT NULL,
                fecha_nacimiento TEXT NOT NULL,
                edad_verificada INTEGER DEFAULT 0,
                activo INTEGER DEFAULT 1
            )
        ''')
        self.conn.commit()

    def crear(self, nombre, email, contrasena_hash, fecha_nacimiento, edad_verificada=1):
        try:
            self.cursor.execute('''
                INSERT INTO usuario (nombre, email, contrasena_hash, fecha_nacimiento, edad_verificada)
                VALUES (?, ?, ?, ?, ?)
            ''', (nombre, email, contrasena_hash, fecha_nacimiento, edad_verificada))
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception:
            return None

    def obtener(self, id_usuario):
        self.cursor.execute('SELECT * FROM usuario WHERE id = ?', (id_usuario,))
        return self.cursor.fetchone()