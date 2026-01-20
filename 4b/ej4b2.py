"""
Jefferson Vivas

Enunciado:
Implementa la función 'average_score_ram(scores_dict)' que recibe un
diccionario con el nombre y la calificación de los estudiantes y calcula
el promedio de calificaciones. Se debe usar un bucle 'for' para ilustrar
el uso de RAM.

La función 'average_score_heap(scores_dict)' ya está implementada y
debe almacenar el promedio de calificaciones en el Heap; sin embargo, existe un error 
en este cálculo identifícalo y corrígelo.

Parámetros:
- scores_dict: Diccionario con el nombre del estudiante como clave y su
calificación como valor.

Ejemplo:
    Entrada:
        average_score_ram({'Juan': 8, 'Maria': 7, 'Pedro': 9})
        average_score_heap({'Juan': 8, 'Maria': 7, 'Pedro': 9})
        
    Salida:
        8.0
        8.0
    
"""


def average_score_ram(scores_dict):
    # Store the dictionary in RAM
    # Write here your code
    return sum(scores_dict.values()) / len(scores_dict)

import heapq
def average_score_heap(scores_dict):
    # Store the dictionary in Heap
    score_list = list(scores_dict.values())
    heapq.heapify(score_list)
    # You should correct and overwrite something in the following line.
    heap_average = sum(score_list) / len(score_list)
    return heap_average


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

scores_dict = {"Juan": 6.7, "Maria": 9.1, "Pedro": 6.5, "Tomas": 8.2, "Julio": 9}

print(average_score_ram(scores_dict))
print(average_score_heap(scores_dict))
