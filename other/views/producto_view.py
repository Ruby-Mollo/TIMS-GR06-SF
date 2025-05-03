# views/producto_view.py
import tkinter as tk
from tkinter import messagebox
from controllers import producto_controller

def producto_window(root):
    ventana = tk.Toplevel(root)
    ventana.title("Productos")

    nombre = tk.Entry(ventana); descripcion = tk.Entry(ventana)
    categoria = tk.Entry(ventana); cantidad = tk.Entry(ventana)
    precio = tk.Entry(ventana)

    for idx, text in enumerate(["Nombre", "Descripción", "Categoría", "Cantidad", "Precio"]):
        tk.Label(ventana, text=text).grid(row=idx, column=0)
    for idx, entry in enumerate([nombre, descripcion, categoria, cantidad, precio]):
        entry.grid(row=idx, column=1)

    def guardar():
        data = (nombre.get(), descripcion.get(), categoria.get(),
                int(cantidad.get()), float(precio.get()))
        producto_controller.agregar_producto(data)
        messagebox.showinfo("Éxito", "Producto registrado")

    tk.Button(ventana, text="Guardar", command=guardar).grid(row=5, columnspan=2)
