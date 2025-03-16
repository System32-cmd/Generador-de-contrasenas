import tkinter as tk
from tkinter import messagebox
import random
import string

# Función para generar la contraseña
def generar_contrasena():
    try:
        longitud = int(spinbox_longitud.get())
        if longitud <= 0 or longitud > 20:
            raise ValueError("La longitud debe estar entre 1 y 20 caracteres.")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido para la longitud (1-20).")
        return
    
    caracteres = ""
    if var_mayusculas.get():
        caracteres += string.ascii_uppercase
    if var_minusculas.get():
        caracteres += string.ascii_lowercase
    if var_numeros.get():
        caracteres += string.digits
    if var_simbolos.get():
        caracteres += string.punctuation
    
    if not caracteres:
        messagebox.showerror("Error", "Seleccione al menos un tipo de carácter.")
        return
    
    contrasena = "".join(random.choice(caracteres) for _ in range(longitud))
    entry_contrasena.delete(0, tk.END)
    entry_contrasena.insert(0, contrasena)

# Función para copiar la contraseña al portapapeles
def copiar_al_portapapeles():
    ventana.clipboard_clear()
    ventana.clipboard_append(entry_contrasena.get())
    ventana.update()
    messagebox.showinfo("Copiado", "Contraseña copiada al portapapeles.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("400x300")
ventana.resizable(False, False)

# Widgets
frame = tk.Frame(ventana)
frame.pack(pady=20)

tk.Label(frame, text="Longitud de la contraseña:").grid(row=0, column=0)
spinbox_longitud = tk.Spinbox(frame, from_=1, to=20, width=5)
spinbox_longitud.grid(row=0, column=1)

var_mayusculas = tk.BooleanVar()
var_minusculas = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_simbolos = tk.BooleanVar()

chk_mayusculas = tk.Checkbutton(frame, text="Mayúsculas", variable=var_mayusculas)
chk_mayusculas.grid(row=1, column=0, sticky="w")
chk_minusculas = tk.Checkbutton(frame, text="Minúsculas", variable=var_minusculas)
chk_minusculas.grid(row=2, column=0, sticky="w")
chk_numeros = tk.Checkbutton(frame, text="Números", variable=var_numeros)
chk_numeros.grid(row=3, column=0, sticky="w")
chk_simbolos = tk.Checkbutton(frame, text="Símbolos", variable=var_simbolos)
chk_simbolos.grid(row=4, column=0, sticky="w")

btn_generar = tk.Button(frame, text="Generar", command=generar_contrasena)
btn_generar.grid(row=5, column=0, columnspan=2, pady=10)

entry_contrasena = tk.Entry(ventana, width=40)
entry_contrasena.pack(pady=5)

btn_copiar = tk.Button(ventana, text="Copiar", command=copiar_al_portapapeles)
btn_copiar.pack()

# Ejecutar la aplicación
ventana.mainloop()
