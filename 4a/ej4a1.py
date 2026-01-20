"""
Jefferson Vivas

Enunciado:
Dadas dos listas de elementos, implementa una función llamada
find_intersection(list_1, list_2) que retorne la intersección de ambas listas.

Parámetros:
    list_1 (List): Lista de elementos
    list_2 (List): Lista de elementos

Ejemplo:
    Entrada:
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [4, 5, 6, 7, 8]

    Salida:
    [4, 5]

"""

list_1 = [1, 2, 3, 4, 5]
list_2 = [4, 5, 6, 7, 8]


def find_intersection(list_1, list_2):
    # Write here your code
    interseccion = []
    
    for element in list_1:
        if element in list_2:
            interseccion.append(element)
    return (interseccion)


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# print(find_intersection([1, 2, 3, 4], [3, 4, 5, 6]))
# print(find_intersection(['apple', 'banana', 'orange'], ['banana', 'kiwi', 'apple']))
