


#1. Escriba un programa que almacene (Input) en una Lista las materias que has cursado con sus respectivas notas
#. Luego muestre la lista por consola mediante un ciclo.

# Crear una lista vacía para almacenar las materias y las notas
lista = []

# Pedir al usuario el número de materias
n = int(input("¿Cuántas materias has cursado? "))

# Usar un ciclo for para pedir el nombre y la nota de cada materia
for i in range(n):
  # Pedir el nombre de la materia
  materia = input("¿Cómo se llama la materia? ")
  # Pedir la nota de la materia
  nota = float(input("¿Qué nota has sacado? "))
  # Añadir la materia y la nota a la lista como una tupla
  lista.append((materia, nota))
# Usar otro ciclo for para mostrar la lista por consola
for item in lista:
  # Imprimir el nombre y la nota de cada materia
  print(item[0], ":", item[1])

#2. Escriba un programa que almacene personas (input), luego que le muestre 
#por pantalla el mensaje de ‘Su nombre es ‘nombre’
  #------------------
  #  cantidad de personas
num_personas = int(input("digite la cantidad de personas: "))

# lista vacía para almacenar los nombres
nombres = []

# decirle al usuario cada nombre y agregarlo a la lista
for _ in range(num_personas):
    nombre = input("digite1 un nombre: ")
    nombres.append(nombre)

# Mostrar los nombres ingresados
print("\nNombres ingresados:")
for nombre in nombres:
    print(f"Su nombre es {nombre}")

#3. Escribir un programa que guarde en una variable un diccionario con los siguientes valores 
#{'Euro':'€', 'Dollar':'$', 'Yen':'¥'} Luego pregunte al usuario por una divisa y el valor en pesos a convertir. Luego muestre en consola el 
#símbolo con el valor que corresponde a la divisa o un mensaje de advertencia si esa divisa no se encuentra en el diccionario.
#--------------
# Guardar el diccionario de divisas
divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# Pedir al usuario una divisa y un valor en pesos
divisa = input("Introduce una divisa: ")
pesos = float(input("Introduce el valor en pesos: "))
# Mostrar el símbolo y el valor convertido o un mensaje de aviso
if divisa in divisas:
    # Usar una tasa de cambio fija para simplificar el ejemplo
    tasas = {'Euro':4.000, 'Dollar':5.000, 'Yen':2.0001}
    print(divisas[divisa] + " " + str(pesos * tasas[divisa]))
else:
    print("La divisa no está en el diccionario.")

#4. En una tupla coloque o ingrese (input) los siguientes valores: números enteros, 
#decimales, String, colecciones. Luego muestre en consola que tipo de datos o variable son los valores digitados
    #--------------------
# decirle al usuario ingresar valores
valor1 = input("Ingrese un valor entero: ")
valor2 = input("Ingrese un valor decimal: ")
valor3 = input("Ingrese un valor de tipo String: ")
valor4 = input("Ingrese una colección (puede ser lista, tupla, conjunto o diccionario): ")

# Convertir los valores ingresados a los tipos de datos correspondientes
try:
    valor1 = int(valor1)
except ValueError:
    valor1 = None

try:
    valor2 = float(valor2)
except ValueError:
    valor2 = None

# Valor3 ya es de tipo String

try:
    valor4 = eval(valor4)  # Intentar evaluar la entrada como una expresión de Python
except:
    valor4 = None

# Mostrar el tipo de dato de cada valor
print("\nTipos de datos ingresados:")
print(f"Valor 1: {valor1}, Tipo: {type(valor1)}")
print(f"Valor 2: {valor2}, Tipo: {type(valor2)}")
print(f"Valor 3: {valor3}, Tipo: {type(valor3)}")
print(f"Valor 4: {valor4}, Tipo: {type(valor4)}")
