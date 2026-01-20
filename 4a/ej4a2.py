"""
Jefferson Vivas

Enunciado:

Crea una función llamada 'count_fruits(fruits_list)' que reciba como parámetro una lista
de frutas y retorne un diccionario donde cada llave sea el nombre de una
fruta y su valor sea la cantidad de veces que aparece en la lista.

Parámetros:
    fruits_list: lista de frutas

Retorno:
    Un diccionario donde cada llave es el nombre de una fruta y su valor es
    la cantidad de veces que aparece en la lista.

Ejemplo:
    Entrada:
    fruits = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana', 'kiwi', 'kiwi', 'kiwi']
    count_fruits(fruits)

    Salida:
    {'apple': 2, 'banana': 2, 'orange': 1, 'kiwi': 4}

"""
# frutas = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana', 'kiwi', 'kiwi', 'kiwi']

# # fruta = frutas.count('kiwi')

# # print(fruta)

def count_fruits(fruits_list):
    # Write here your code
    contador_fruta = 0
    frutas = {}
    for fruta in fruits_list:
        frutas[fruta] = fruits_list.count(fruta)
    return frutas

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

fruits = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana', 'kiwi', 'kiwi', 'kiwi']
print(count_fruits(fruits))