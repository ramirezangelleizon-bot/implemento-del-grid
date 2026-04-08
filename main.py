import tkinter as tk
from dotenv import load_dotenv
import os
from pathlib import Path

# 1. Configuración para encontrar el archivo .env correctamente
# Esto busca el archivo en la misma carpeta donde está este script
ruta_env = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=ruta_env)

# Obtener variables
USUARIO_CORRECTO = os.getenv("USER_NAME")
PASSWORD_CORRECTO = os.getenv("USER_PASSWORD")

# 2. Función de validación
def validar_acceso():
    usuario_ingresado = campo_entrada_usuario.get().strip()
    password_ingresado = campo_entrada_password.get().strip()
    
    # Verificación de seguridad si no carga el .env
    if USUARIO_CORRECTO is None:
        label_resultado.config(text="Error: No se detectó el archivo .env", fg="orange")
        return

    if usuario_ingresado == USUARIO_CORRECTO and password_ingresado == PASSWORD_CORRECTO:
        label_resultado.config(text="✅ Acceso correcto", fg="green")
        boton.config(bg="green", fg="white", text="Acceso Concedido")
    else:
        label_resultado.config(text="❌ Usuario o contraseña incorrectos", fg="red")
        boton.config(bg="#f0f0f0", fg="black", text="Validar")
        campo_entrada_password.delete(0, tk.END)

# 3. Interfaz Gráfica con .grid()
ventana = tk.Tk()
ventana.title("Login con Grid")
ventana.geometry("350x300")

# Configuración de columnas
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)

# Título
lbl_titulo = tk.Label(ventana, text="INICIO DE SESIÓN", font=("Arial", 12, "bold"))
lbl_titulo.grid(row=0, column=0, columnspan=2, pady=20)

# Usuario
tk.Label(ventana, text="Usuario:", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="e", padx=10, pady=5)
campo_entrada_usuario = tk.Entry(ventana, font=("Arial", 11))
campo_entrada_usuario.grid(row=1, column=1, sticky="w", padx=10, pady=5)

# Contraseña
tk.Label(ventana, text="Contraseña:", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="e", padx=10, pady=5)
campo_entrada_password = tk.Entry(ventana, show="*", font=("Arial", 11))
campo_entrada_password.grid(row=2, column=1, sticky="w", padx=10, pady=5)

# Botón
boton = tk.Button(ventana, text="Validar", command=validar_acceso, bg="#f0f0f0", width=15)
boton.grid(row=3, column=0, columnspan=2, pady=20)

# Etiqueta de resultado
label_resultado = tk.Label(ventana, text="", font=("Arial", 10, "bold"))
label_resultado.grid(row=4, column=0, columnspan=2, pady=5)

# Vincular tecla Enter
ventana.bind('<Return>', lambda event: validar_acceso())

ventana.mainloop()