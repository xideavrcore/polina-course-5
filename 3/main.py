# Лабораторная работа 3
# Работа со стеком (LIFO, лекция 5)

class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.A = [0] * max_size
        self.size = -1  # индекс вершины; -1 = пустой

    def push(self, value):
        if self.size < self.max_size - 1:
            self.size = self.size + 1
            self.A[self.size] = value

    def pop(self):
        if self.size >= 0:
            value = self.A[self.size]
            self.size = self.size - 1
            return value
        return None

    def is_empty(self):
        return self.size < 0


def main():
    # Исходный массив из 10 элементов
    a = [5, 12, 7, 3, 20, 9, 1, 15, 8, 4]
    print("Исходный массив:")
    print(a)

    st = Stack(10)
    for x in a:
        st.push(x)

    # Извлечение из стека (LIFO - обратный порядок)
    result = []
    while not st.is_empty():
        result.append(st.pop())

    print("Массив, извлеченный из стека:")
    print(result)


if __name__ == "__main__":
    main()
