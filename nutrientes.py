import tkinter as tk
from tkinter import messagebox

# Aquí asumimos que tienes una función que obtiene los datos de los nutrientes
# Esta función es solo un marcador de posición. Debes implementarla según tu fuente de datos.
def obtener_nutrientes(planta):
    # Reemplaza esto con la lógica para obtener los datos reales de nutrientes
    datos_nutrientes = {
        "Tomate": "Nitrógeno, Fósforo, Potasio, Calcio",
        "Lechuga": "Nitrógeno, Potasio, Hierro, Magnesio"
    }
    return datos_nutrientes.get(planta, "Información no disponible")

# Función que se llama cuando el usuario presiona el botón de buscar
def mostrar_nutrientes():
    planta = entrada_planta.get()
    nutrientes = obtener_nutrientes(planta)
    messagebox.showinfo("Nutrientes Necesarios", nutrientes)

# Creación de la ventana principal
root = tk.Tk()
root.title("Nutrientes de la Planta")

# Configuración del campo de entrada
etiqueta_planta = tk.Label(root, text="Ingresa el nombre de la planta:")
etiqueta_planta.pack()
entrada_planta = tk.Entry(root)
entrada_planta.pack()

# Configuración del botón de buscar
boton_buscar = tk.Button(root, text="Mostrar Nutrientes", command=mostrar_nutrientes)
boton_buscar.pack()

# Iniciar el bucle de la GUI
root.mainloop()
