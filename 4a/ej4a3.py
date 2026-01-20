"""
Jefferson Vivas

Enunciado:

Escribe una función llamada 'descending_list_iterator(numbers_list)' que tome una lista
de números como argumento y devuelva un iterador que genere los mismos
números de mayor a menor.

Parámetros:
    numbers_list (list): Lista de números enteros a ser ordenados.

Ejemplo:
    Entrada:
    [5, 1, 8, 3, 2]

    Salida:
    El iterador debería generar los números en el siguiente orden:
    8, 5, 3, 2, 1.

"""


def descending_list_iterator(numbers_list):
    # Write here your code
    return iter(sorted(numbers_list, reverse=True))


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

numeros = [2, 3, 6, 9, 11, 12, 15, 18]
print(list(descending_list_iterator(numeros)))  
