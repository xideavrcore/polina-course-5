# Лабораторная работа 2
# Поиск минимального элемента (линейный поиск, лекции 1 и 4)

def find_min(a):
    # Линейный проход: min и его индекс
    min_val = a[0]
    min_idx = 0
    for i in range(1, len(a)):
        if a[i] < min_val:
            min_val = a[i]
            min_idx = i
    return min_val, min_idx


def main():
    # Исходный массив из 10 элементов
    a = [15, 28, 3, -5, -17, 8, 1, 42, 9, 11]
    print("Исходный массив:")
    print(a)

    min_val, min_idx = find_min(a)
    # Номер в массиве: с 1 (как в отчёте по заданию)
    print("Минимальный элемент:", min_val)
    print("Номер в массиве:", min_idx + 1)


if __name__ == "__main__":
    main()
