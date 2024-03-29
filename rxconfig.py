import reflex as rx
import pyodbc
# Valores de la base de datos
usuario = "sa"
password = "password123"
host = "localhost"
db = "master"
port = 1433

# Configuración de la base de datos
config = rx.Config(
    app_name="my_app",
    
)

