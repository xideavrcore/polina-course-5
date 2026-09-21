# Лабораторная работа 6
# Упорядоченное двоичное дерево (BST, лекции 4 и 8)

class Node:
    def __init__(self, elem):
        self.elem = elem
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.elem:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def inorder(root, result):
    # Обход ЛКП дает упорядоченный массив
    if root is None:
        return
    inorder(root.left, result)
    result.append(root.elem)
    inorder(root.right, result)


def main():
    # 12 произвольных элементов
    data = [50, 30, 70, 20, 40, 60, 80, 15, 35, 55, 65, 90]
    print("Исходные данные:")
    print(data)

    root = None
    for x in data:
        root = insert(root, x)

    ordered = []
    inorder(root, ordered)
    print("Упорядоченный массив (обход дерева):")
    print(ordered)


if __name__ == "__main__":
    main()
