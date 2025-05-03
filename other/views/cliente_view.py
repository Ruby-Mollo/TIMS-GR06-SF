# views/cliente_view.py
import tkinter as tk
from tkinter import messagebox
from controllers import cliente_controller

def cliente_window(root):
    ventana = tk.Toplevel(root)
    ventana.title("Clientes")

    nombre = tk.Entry(ventana); dni = tk.Entry(ventana); email = tk.Entry(ventana)
    telefono = tk.Entry(ventana); direccion = tk.Entry(ventana)
    razon_social = tk.Entry(ventana); ruc = tk.Entry(ventana)

    for idx, text in enumerate(["Nombre", "DNI", "Email", "Teléfono", "Dirección", "Razón Social", "RUC"]):
        tk.Label(ventana, text=text).grid(row=idx, column=0)
    for idx, entry in enumerate([nombre, dni, email, telefono, direccion, razon_social, ruc]):
        entry.grid(row=idx, column=1)

    def guardar():
        data = (nombre.get(), dni.get(), email.get(), telefono.get(),
                direccion.get(), razon_social.get(), ruc.get())
        cliente_controller.agregar_cliente(data)
        messagebox.showinfo("Éxito", "Cliente registrado")

    tk.Button(ventana, text="Guardar", command=guardar).grid(row=7, columnspan=2)

    # TODO: Agregar botones de editar y eliminar si deseas mostrarlos en interfaz
