"""
Jefferson Vivas

Enunciado:
Implementa una función llamada 'create_list(length_list)' que reciba de
parámetro un valor numérico entero llamado 'length_list'. Se deben retornar
dos listas de enteros que ilustren el almacenamiento de valores en la RAM
y en el Heap. Por lo tanto, la primera lista debe tener numeros enteros
aleatorios entre 0 y 100, que debe ser almacenada en la RAM; y la
segunda lista debe ser almacenada en el Heap reutilizando la primera lista
creada.

Para crear una lista en el Heap, se puede usar la libreria 'copy' y su función
'deepcopy(list)', en este ejemplo lo usaremos de la siguiente forma:
“copy.deepcopy('list_to_copy')”. 

Para crear numeros aleatorios se puede usar la librería 'random'. Deberás
añadir "import random" a tu código, y luego usar "random.randint(0, 100)"
para crear números aleatorios entre 0 y 100.

Considerar que en caso de que el número 'length_list' ingresado en la función
'create_list' se debe mostrar el error: 
ValueError("The number must be positive")

Parámetros:
    - length_list (int): Número entero que sea positivo.

Ejemplo:
    Entrada:
    create_list(4)

    Salida:
    ([17, 16, 30, 17], [17, 16, 30, 17])

"""
import copy
import random


def create_list(length_list):
    """
    Creates two lists of integers to illustrate the difference between RAM and
    Heap memory.

    Args:
    length_list: A numeric integer value indicating the length of the lists to
    be created.

    Returns:
    A tuple containing two lists of integers, the first one created in RAM and
    the second one created in Heap by reusing the first list.
    """

    # Write here your code
    ram_list = []
    heap_list = []
    i = 0
    
    if length_list < 0:
        raise ValueError("The number must be positive")
    else:
        while i < length_list:
            ram_list.append(random.randint(0, 100))
            i += 1
    heap_list = copy.deepcopy(ram_list)
    return (ram_list, heap_list)


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(create_list(6))
