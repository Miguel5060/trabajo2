
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import mysql.connector
from datetime import datetime

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="reserva de hoteles"
)
cursor = conexion.cursor()
reserva_confirmada = False

# Funciones
def verificar_disponibilidad():
    global reserva_confirmada
    fecha_inicio = cal_inicio.get_date()
    fecha_fin = cal_fin.get_date()
    tipo_servicio = entrada_tipo_servicio.get()

    sql = "SELECT COUNT(*) FROM reservas WHERE tipo_servicio = %s AND ((fecha_inicio BETWEEN %s AND %s) OR (fecha_fin BETWEEN %s AND %s))"
    val = (tipo_servicio, fecha_inicio, fecha_fin, fecha_inicio, fecha_fin)

    cursor.execute(sql, val)
    resultado = cursor.fetchone()

    if resultado[0] > 0:
        print("No hay disponibilidad para estas fechas.")
        reserva_confirmada = False
    else:
        print("¡Disponibilidad confirmada! Realizar reserva.")
        reserva_confirmada = True

def hacer_reserva():
    global reserva_confirmada
    verificar_disponibilidad()

    if reserva_confirmada:
        fecha_inicio_str = cal_inicio.get_date()
        fecha_fin_str = cal_fin.get_date()

        fecha_inicio = datetime.strptime(fecha_inicio_str, '%m/%d/%y').strftime('%Y-%m-%d')
        fecha_fin = datetime.strptime(fecha_fin_str, '%m/%d/%y').strftime('%Y-%m-%d')
        
        tipo_servicio = entrada_tipo_servicio.get()

        sql_insert = "INSERT INTO reservas (fecha_inicio, fecha_fin, tipo_servicio) VALUES (%s, %s, %s)"
        val_insert = (fecha_inicio, fecha_fin, tipo_servicio)
        
        cursor.execute(sql_insert, val_insert)
        conexion.commit()
        print("Reserva realizada correctamente.")
    else:
        print("No se puede realizar la reserva debido a la falta de disponibilidad.")


def cancelar_servicio():
    fecha_inicio = cal_inicio.get_date().strftime('%Y-%m-%d')  # Formatear la fecha
    fecha_fin = cal_fin.get_date().strftime('%Y-%m-%d')  # Formatear la fecha
    tipo_servicio = entrada_tipo_servicio.get()

    sql_delete = "DELETE FROM reservas WHERE fecha_inicio = %s AND fecha_fin = %s AND tipo_servicio = %s"
    val_delete = (fecha_inicio, fecha_fin, tipo_servicio)

    cursor.execute(sql_delete, val_delete)
    conexion.commit()
    print("Servicio cancelado para las fechas:", fecha_inicio, "a", fecha_fin, "Tipo de servicio:", tipo_servicio)

    # Registro en la tabla 'cancelaciones' con las fechas correspondientes
    sql_insert_cancelacion = "INSERT INTO cancelaciones (fecha_inicio, fecha_fin, tipo_servicio) VALUES (%s, %s, %s)"
    val_insert_cancelacion = (fecha_inicio, fecha_fin, tipo_servicio)

    cursor.execute(sql_insert_cancelacion, val_insert_cancelacion)
    conexion.commit()
    print("Cancelación registrada en la base de datos.")

def registrar_persona():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    email = entrada_email.get()
    telefono = entrada_telefono.get()

    sql_insert_persona = "INSERT INTO personas (nombre, apellido, email, telefono) VALUES (%s, %s, %s, %s)"
    val_insert_persona = (nombre, apellido, email, telefono)

    cursor.execute(sql_insert_persona, val_insert_persona)
    conexion.commit()
    print("Persona registrada correctamente.")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Sistema de Reservas")

# Elementos de la ventana
etiqueta_nombre = ttk.Label(ventana, text="Nombre:")
etiqueta_nombre.grid(row=0, column=0, padx=10, pady=10)
entrada_nombre = ttk.Entry(ventana)
entrada_nombre.grid(row=0, column=1, padx=10, pady=10)

etiqueta_apellido = ttk.Label(ventana, text="Apellido:")
etiqueta_apellido.grid(row=1, column=0, padx=10, pady=10)
entrada_apellido = ttk.Entry(ventana)
entrada_apellido.grid(row=1, column=1, padx=10, pady=10)

etiqueta_email = ttk.Label(ventana, text="Email:")
etiqueta_email.grid(row=2, column=0, padx=10, pady=10)
entrada_email = ttk.Entry(ventana)
entrada_email.grid(row=2, column=1, padx=10, pady=10)

etiqueta_telefono = ttk.Label(ventana, text="Teléfono:")
etiqueta_telefono.grid(row=3, column=0, padx=10, pady=10)
entrada_telefono = ttk.Entry(ventana)
entrada_telefono.grid(row=3, column=1, padx=10, pady=10)

boton_registrar_persona = ttk.Button(ventana, text="Registrar Persona", command=registrar_persona)
boton_registrar_persona.grid(row=4, column=0, columnspan=2, pady=10)

etiqueta_fecha_inicio = ttk.Label(ventana, text="Fecha de Inicio:")
etiqueta_fecha_inicio.grid(row=5, column=0, padx=10, pady=10)
entrada_fecha_inicio = ttk.Entry(ventana)
entrada_fecha_inicio.grid(row=5, column=1, padx=10, pady=10)

etiqueta_fecha_fin = ttk.Label(ventana, text="Fecha de Fin:")
etiqueta_fecha_fin.grid(row=6, column=0, padx=10, pady=10)
entrada_fecha_fin = ttk.Entry(ventana)
entrada_fecha_fin.grid(row=6, column=1, padx=10, pady=10)

etiqueta_tipo_servicio = ttk.Label(ventana, text="Tipo de Servicio:")
etiqueta_tipo_servicio.grid(row=7, column=0, padx=10, pady=10)
entrada_tipo_servicio = ttk.Entry(ventana)
entrada_tipo_servicio.grid(row=7, column=1, padx=10, pady=10)

boton_reservar = ttk.Button(ventana, text="Reservar", command=hacer_reserva)
boton_reservar.grid(row=8, column=0, columnspan=2, pady=10)

cal_inicio = Calendar(ventana, selectmode="day", year=2023, month=11, day=19)
cal_inicio.grid(row=9, column=0, padx=10, pady=10)
cal_fin = Calendar(ventana, selectmode="day", year=2023, month=11, day=19)
cal_fin.grid(row=9, column=1, padx=10, pady=10)

boton_verificar = ttk.Button(ventana, text="Verificar Disponibilidad", command=verificar_disponibilidad)
boton_verificar.grid(row=10, column=0, columnspan=2, pady=10)

boton_cancelar = ttk.Button(ventana, text="Cancelar Servicio", command=cancelar_servicio)
boton_cancelar.grid(row=11, column=0, columnspan=2, pady=10)  

ventana.mainloop()
