# Лабораторная работа 4
# Работа с очередью (FIFO, лекция 6)
# В очередь заносится текущий максимум массива; после занесения
# его значение в массиве меняется на отрицательное.

class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.A = [0] * max_size
        self.head = 0
        self.tail = 0
        self.count = 0

    def enqueue(self, value):
        if self.count < self.max_size:
            self.A[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.count = self.count + 1

    def dequeue(self):
        if self.count > 0:
            value = self.A[self.head]
            self.head = (self.head + 1) % self.max_size
            self.count = self.count - 1
            return value
        return None

    def is_empty(self):
        return self.count == 0


def find_max_index(a):
    # Индекс текущего максимума среди положительных
    max_i = -1
    for i in range(len(a)):
        if a[i] > 0 and (max_i < 0 or a[i] > a[max_i]):
            max_i = i
    return max_i


def main():
    # Исходный массив из 10 положительных элементов
    a = [14, 3, 27, 9, 5, 31, 8, 12, 2, 19]
    print("Исходный массив:")
    print(a)

    work = a[:]  # рабочая копия
    q = Queue(10)

    for _ in range(10):
        i = find_max_index(work)
        q.enqueue(work[i])
        work[i] = -work[i]  # помечаем как обработанный

    result = []
    while not q.is_empty():
        result.append(q.dequeue())

    print("Значения, извлеченные из очереди:")
    print(result)


if __name__ == "__main__":
    main()
