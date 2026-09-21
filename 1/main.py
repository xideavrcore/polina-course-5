# Лабораторная работа 1
# Сортировка одномерного массива методом вставок (лекция 3)

def insertion_sort(x):
    n = len(x)
    for i in range(1, n):
        key = x[i]
        j = i - 1
        while j >= 0 and x[j] > key:
            x[j + 1] = x[j]
            j = j - 1
        x[j + 1] = key


def main():
    # Исходный массив из 10 элементов
    a = [6, 19, 3, 8, 92, 15, 1, 9, 44, 27]
    print("Исходный массив:")
    print(a)

    insertion_sort(a)

    print("Отсортированный массив:")
    print(a)


if __name__ == "__main__":
    main()
