import pyodbc

def conexion():
    try:
        conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-31DR6UE;'
        'DATABASE=DBCRUD;'
        'UID=bjcabello;'
        'PWD=root;'
        'TrustServerCertificate=yes;'
    )
        print(" Conexión exitosa a SQL Server")
        return conn

    except pyodbc.Error as e:
        print(" Error al conectar a SQL Server:")
        print(e)
        return None
