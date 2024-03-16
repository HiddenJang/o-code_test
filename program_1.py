import numpy as np

########## Программа 1 - формирование исходных данных ############

def write_vectors(N: int, m: int) -> None:
    """Генерация и запись векторов в файл vectors.csv"""

    vectors_array = np.random.uniform(-1, 1, (N, m))
    np.savetxt("vectors.csv", vectors_array, delimiter=",", fmt='%.8f')

if __name__ == '__main__':
    N = int(input("Введите число N (500<N<=1000): "))
    m = int(input("Введите число m (10<m<=50): "))
    write_vectors(N, m)
