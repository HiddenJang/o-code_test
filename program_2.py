import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
#import matplotlib.animation as animation

matplotlib.use('QtAgg')

########## Программа 2 - основное задание ###############

def calculate_distances(vectors_array: list) -> list:
    """Вычисление Евклидовых расстояний, поиск минимального и максимального расстояний"""

    distances = []
    for vector_first in range(0, len(vectors_array)-1):
        for vector_second in range(vector_first+1, len(vectors_array)):
            point_1 = np.array(vectors_array[vector_first], dtype=np.float_)
            point_2 = np.array(vectors_array[vector_second], dtype=np.float_)
            vectors_square = np.square(point_1 - point_2)
            sum_vectors_square = np.sum(vectors_square)
            euclid_distance_solved = np.sqrt(sum_vectors_square)

            distances.append(euclid_distance_solved)

            if not vector_first and vector_second:
                max_distance_vectors_numbers = [vector_first, vector_second]
                max_distance = euclid_distance_solved
                min_distance_vectors_numbers = [vector_first, vector_second]
                min_distance = euclid_distance_solved
                continue

            if euclid_distance_solved > max_distance:
                max_distance_vectors_numbers = [vector_first, vector_second]
                max_distance = euclid_distance_solved

            elif euclid_distance_solved < min_distance:
                min_distance_vectors_numbers = [vector_first, vector_second]
                min_distance = euclid_distance_solved

            else:
                continue

    print(f'Номера векторов с максимальным расстоянием: {max_distance_vectors_numbers}, '
          f'максимальное расстояние: {max_distance}, \n'
          f'Номера векторов с минимальным расстоянием: {min_distance_vectors_numbers}, '
          f'минимальное расстояние: {min_distance}')
    return distances


if __name__ == '__main__':
    vectors_array = np.genfromtxt('vectors.csv', delimiter=',')
    distances = calculate_distances(vectors_array)

    ## Построение гистограммы распределения Евклидовых расстояний между различными парами векторов в зависимости от количества сочетаний ##
    df = pd.DataFrame(distances)
    print(df)
    plt.hist(df)
    plt.show()
    # ydata = distances
    # xdata = [i for i in range(len(distances))]
    # plt.xlabel('Количество расстояний')
    # plt.ylabel('Величина Евклидова расстояния')
    # plt.xticks(arange(0, len(distances), len(distances)/10))
    # plt.bar(xdata, ydata)
    # plt.show()

