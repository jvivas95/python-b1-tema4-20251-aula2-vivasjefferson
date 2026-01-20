"""
Jefferson Vivas

Enunciado:
Implementa la función 'create_read_file()', que no recibe ningún
parámetro debido a que esta función debe crear un archivo de texto 
'text_file.txt', dentro de dicho archivo se deben escribir tres líneas de
información. La primera línea debe contener un nombre, la segunda línea un
apellido y finalmente, la edad. A continuación se debe leer el archivo e imprimir
por consola todas las líneas del mismo.

Parámetro:
- No recibe ningún parámetro debido a que dentro de esta función se crea un
archivo de texto.

Ejemplo:
    Salida:
        Juan
        Perez
        30
"""
def create_read_file():
    # Write here your code
    with open("text_file.txt", "w") as file:
        file.write("Juan\n")
        file.write("Perez\n")
        file.write("30\n")
    
    with open("text_file.txt", "r") as file:
        for line in file:
            print(line)



# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# create_read_file()