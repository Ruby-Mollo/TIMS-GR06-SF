# views/main_window.py
import tkinter as tk
from views import cliente_view, producto_view, factura_view
from PIL import Image, ImageTk

def main():
    root = tk.Tk()
    root.title("Sistema de Facturación")
    root.geometry("500x400")

    # Logo
    try:
        logo = Image.open("assets/logo.png")
        logo = logo.resize((150, 150))
        logo_img = ImageTk.PhotoImage(logo)
        tk.Label(root, image=logo_img).pack()
    except Exception as e:
        print("No se pudo cargar el logo:", e)

    tk.Button(root, text="Clientes", command=lambda: cliente_view.cliente_window(root)).pack(pady=5)
    tk.Button(root, text="Productos", command=lambda: producto_view.producto_window(root)).pack(pady=5)
    tk.Button(root, text="Facturas", command=lambda: factura_view.factura_window(root)).pack(pady=5)

    root.mainloop()
