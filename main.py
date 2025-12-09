from fastapi import FastAPI
from database import conexion
from models import Producto

app = FastAPI()

# CREATE
@app.post("/productos")
def crear_producto(producto: Producto):
    conn = conexion()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Productos (nombre, precio, stock)
        VALUES (?, ?, ?)
    """, (producto.nombre, producto.precio, producto.stock))

    conn.commit()
    return {"mensaje": "Producto creado"}

# READ - Listar todos
@app.get("/productos")
def listar_productos():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Productos")
    rows = cursor.fetchall()

    productos = []
    for r in rows:
        productos.append({
            "id": r.id,
            "nombre": r.nombre,
            "precio": float(r.precio),
            "stock": r.stock
        })

    return productos

# READ - Obtener por ID
@app.get("/productos/{id}")
def obtener_producto(id: int):
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Productos WHERE id = ?", (id,))
    row = cursor.fetchone()

    if not row:
        return {"error": "Producto no encontrado"}

    return {
        "id": row.id,
        "nombre": row.nombre,
        "precio": float(row.precio),
        "stock": row.stock
    }

# UPDATE
@app.put("/productos/{id}")
def actualizar_producto(id: int, producto: Producto):
    conn = conexion()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Productos
        SET nombre = ?, precio = ?, stock = ?
        WHERE id = ?
    """, (producto.nombre, producto.precio, producto.stock, id))

    conn.commit()
    return {"mensaje": "Producto actualizado"}

# DELETE
@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    conn = conexion()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Productos WHERE id = ?", (id,))
    conn.commit()

    return {"mensaje": "Producto eliminado"}
