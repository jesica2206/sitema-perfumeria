Sistema de Gestión de Perfumería
Este sistema permite gestionar un negocio de venta de perfumes, incluyendo el manejo de usuarios, categorías, catálogo de fragancias, carritos de compra, pedidos, pagos, reseñas y favoritos.

⚙️ Requisitos Previos
Entorno: Visual Studio Code.

Lenguaje: Python 3.7 o superior.

Verificación de Python: Abre la terminal y ejecuta python --version (o py --version).

Base de Datos: SQLite3 (incluido en Python).

Gestión de paquetes: pip.

🧪 Cómo probar todo el sistema
Para validar la integridad de toda la estructura de datos (tablas, relaciones y claves foráneas), ejecuta el script de integración:

Bash
python run_all.py
🔍 Consultas para probar funcionalidades individuales
Si necesitas probar un módulo específico, puedes ejecutar los tests unitarios correspondientes:

👤 Usuarios y Direcciones
python -m unittest tests.test_usuario.TestUsuario

python -m unittest tests.test_direccion.TestDireccion

🧪 Catálogo (Categorías y Perfumes)
python -m unittest tests.test_categoria.TestCategoria

python -m unittest tests.test_perfume.TestPerfume

🛒 Gestión de Compra (Carrito y Pedidos)
python -m unittest tests.test_carrito.TestCarrito

python -m unittest tests.test_item_carrito.TestItemCarrito

python -m unittest tests.test_pedido.TestPedido

python -m unittest tests.test_item_pedido.TestItemPedido

💳 Pagos, Reseñas y Marketing
python -m unittest tests.test_pago.TestPago

python -m unittest tests.test_resena.TestResena

python -m unittest tests.test_cupon.TestCupon

python -m unittest tests.test_favorito.TestFavorito

📦 Instalación
Clonar el repositorio:

Bash
git clone https://github.com/jesica2206/sitema-perfumeria
