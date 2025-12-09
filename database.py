import pyodbc

def conexion():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-31DR6UE;'
        'DATABASE=DBCRUD;'
        'UID=bjcabello;'
        'PWD=root;'
        'TrustServerCertificate=yes;'
    )
