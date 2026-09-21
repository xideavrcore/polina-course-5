# Лабораторная работа 5
# Работа с графом (лекция 7)
# Неориентированный взвешенный граф по рис. 1.
# Вес ребра - длина на рисунке (условные единицы).
# Вариант 8: кратчайший путь из вершины 8 в вершину 12.
# Алгоритм: Дейкстра (для неотрицательных весов).

N = 13  # вершины 1..13

# Рёбра (u, v, вес), граф неориентированный
EDGES = [
    (1, 2, 258),
    (1, 8, 315),
    (1, 9, 294),
    (1, 13, 181),
    (2, 4, 312),
    (2, 6, 437),
    (2, 8, 532),
    (2, 13, 336),
    (3, 5, 123),
    (3, 6, 248),
    (3, 7, 256),
    (3, 8, 512),
    (3, 9, 147),
    (3, 11, 230),
    (3, 13, 340),
    (4, 7, 199),
    (4, 13, 505),
    (5, 9, 266),
    (5, 11, 220),
    (6, 9, 220),
    (6, 12, 230),
    (7, 9, 378),
    (7, 10, 134),
    (8, 9, 416),
]


def build_matrix():
    # Матрица смежности: вес или None (нет ребра)
    m = [[None] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        m[i][i] = 0
    for u, v, w in EDGES:
        m[u][v] = w
        m[v][u] = w
    return m


def print_matrix(m):
    print("Матрица смежности (вес ребра; * - нет ребра):")
    header = "    " + "".join(f"{j:>5}" for j in range(1, N + 1))
    print(header)
    for i in range(1, N + 1):
        row = f"{i:>3} "
        for j in range(1, N + 1):
            if m[i][j] is None:
                row += f"{'*':>5}"
            else:
                row += f"{m[i][j]:>5}"
        print(row)


def dijkstra(m, start, finish):
    # Кратчайшие пути от start; dist[v], prev[v]
    INF = 10 ** 9
    dist = [INF] * (N + 1)
    prev = [-1] * (N + 1)
    used = [False] * (N + 1)
    dist[start] = 0

    for _ in range(N):
        # выбрать вершину с минимальным dist
        u = -1
        best = INF
        for v in range(1, N + 1):
            if not used[v] and dist[v] < best:
                best = dist[v]
                u = v
        if u < 0:
            break
        used[u] = True
        for v in range(1, N + 1):
            if m[u][v] is not None and m[u][v] > 0:
                nd = dist[u] + m[u][v]
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u

    # восстановить путь
    if dist[finish] >= INF:
        return None, []
    path = []
    cur = finish
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return dist[finish], path


def main():
    print("Вариант 8: кратчайший путь из вершины 8 в вершину 12")
    print("Граф: неориентированный, взвешенный (рис. 1 лекции 7)")
    print()

    m = build_matrix()
    print_matrix(m)
    print()

    length, path = dijkstra(m, 8, 12)
    print("Кратчайший путь:", " - ".join(str(x) for x in path))
    print("Длина кратчайшего пути:", length)


if __name__ == "__main__":
    main()
