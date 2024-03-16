import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('QtAgg')

########## Программа 2 - основное задание ###############

def calculate_distances(vectors_array: np.ndarray) -> pd.DataFrame:
    """Вычисление Евклидовых расстояний, поиск минимального и максимального расстояний"""

    distances_df = pd.DataFrame()
    distances_df["dist_amount"] = []
    distances_df["distance"] = []

    ## В связи с ограничением по количеству элементов структур данных, возможным видится следующий вариант:
    ## посчитать количество каждого расстояния округленного до 0.1 (меньшие значения не подлежат отрисовке)
    ## и потом построить гистограмму распределения на основе сформированных данных

    for vector_first in range(0, len(vectors_array)-1):
        for vector_second in range(vector_first+1, len(vectors_array)):

            ## Вычисление значения Евклидова расстояния ##
            point_1 = np.array(vectors_array[vector_first], dtype=np.float_)
            point_2 = np.array(vectors_array[vector_second], dtype=np.float_)
            vectors_square = np.square(point_1 - point_2)
            sum_vectors_square = np.sum(vectors_square)
            euclid_distance_solved = np.sqrt(sum_vectors_square)

            ## Формирование для построения гистограммы дата-фрейма с количеством расстояний,
            ## округленных до 0.1 (поскольку шаг распределения расстояний на гистограмме задан 0.1).
            ## Если расстояние, округленное до 0.1 есть в дата-фрейме, то увеличиваем количество на единицу,
            ## если нет - то добавляем новую строку в дата-фрейм.
            if distances_df["distance"].isin([round(euclid_distance_solved, 1)]).any():
                row_df = distances_df[distances_df["distance"] == round(euclid_distance_solved, 1)]
                row_index = row_df.index.to_list()[0]
                distances_df.iat[row_index, 0] = row_df.iat[0, 0] + 1
            else:
                new_row_df = pd.DataFrame([{"dist_amount": 1, "distance": round(euclid_distance_solved, 1)}])
                distances_df = distances_df._append(new_row_df, ignore_index=True)

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
    return distances_df


if __name__ == '__main__':
    vectors_array = np.genfromtxt('vectors.csv', delimiter=',')
    distances_df = calculate_distances(vectors_array)

    ## Построение гистограммы распределения Евклидовых расстояний между различными парами векторов с шагом 0.1
    plt.bar(distances_df["distance"], distances_df["dist_amount"], width=0.1)
    plt.xlabel("Величина Евклидова расстояния")
    plt.ylabel("Количество Евклидовых расстояний")
    plt.title("Гистограмма распределения Евклидовых расстояний")
    plt.show()

