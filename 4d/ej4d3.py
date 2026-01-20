"""
Jefferson Vivas

Implementa una función 'read_and_write', no recibe ningún parámetro debido a
que, dentro de la misma se debe solicitar la entrada de 2 datos mediante
teclado.

En el momento de solicitar el ingreso de los datos se debe considerar el
siguiente texto.
'Insert your name: ' El valor introducido debe ser de tipo str.
'Insert your age: ' El valor introducido debe ser de tipo int.

Se debe crear un archivo de texto 'file.txt' donde La información entrada
por consola debe ser guardada en dicho archivo y se debe imprimir por consola
desde el archivo de texto.

Parámetro:
No recibe ningún parámetro.

Ejemplo:
    Entrada:
        'Insert your name: ' Julio 
        'Insert your age: ' 30
    Salida:
        Julio
        30
"""

def read_and_write():
    # Write here your code
    name = input("Insert your name: ")
    age = int(input("Insert your age: "))
    
    # Escrbir los datos solicitados por terminal
    with open ("file.txt", "w") as file:
        file.write(name)
        file.write(str(age))
    
    # Leer las lineas del archivo creado
    with open ("file.txt", "r") as file:
        for linea in file:
            print(linea)

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# read_and_write()