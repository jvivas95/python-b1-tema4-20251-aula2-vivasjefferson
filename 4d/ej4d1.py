"""
Jefferson Vivas

Enunciado:
Realizando la entrada por consola de los datos, implementa la función 'sum'
que solicite la entrada de dos números con 'input' y devuelva la suma de los
números.

Parámetro:
No recibe ningún parámetro debido a que dentro de la función se solicita la
entrada de los números.

Ejemplo:
    Entrada:
        "Insert the first number: " 8
        "Insert the second number: " 3

    Salida:
        "Result: " 11
"""

from unittest import result


def sum():
    # Write here your code
    num_1 = int(input("Insert the first number: "))
    num_2 = int(input("Insert the second number: "))
    result = num_1 + num_2
    print("Result: ", result)
    return (result)

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# # Si vols provar el teu codi, descomenta les línies següents i executa l'script
if __name__ == "__main__":
    sum()
