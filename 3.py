"""
Реалізувати програмно мовою Python завдання з наведеного нижче списку. Для кожної з задач алгоритм реалізувати з
використанням рекурсії і ітерації. Аргументувати письмово доцільність вибору в кожному випадку рекурсії або ітерації
(використовувати в якості критеріїв - час розробки та виконання програм, обсяг займаної пам'яті, читабельність програми)
3. Сформувати функцію для обчислення індексу максимального елемента масиву n*n, де 1<=n<=5.
Барбак Владислав 122-В
"""
while True:
    from time import time  # Імпорутуємо time для підрахунку часу
    import numpy as np
    def max_el_iter(array, max_el=0):  # Створення ітераційної функції
        for i in range(len(array)):
            for j in range(len(array)):
                if max_el < array[i][j]:
                    max_el = array[i][j]
        return max_el
    def max_el_rec(array, count=0, temp=0, i=0, j=0):  # Створення рекурсивної функції
        if temp == len(array[count]):
            count += 1
            temp = 0
        if count == len(array):
            return i, j
        if array[count][temp] > array[i][j]:
            i = count
            j = temp
        temp += 1
        return max_el_rec(array, count, temp, i, j)
    while True:
        n = int(input("Введіть розмірність: "))
        if n in range(1, 6):
            break
    x = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            x[i, j] = int(input("Введіть число: "))
    print("Створений масив: \n", x)
    t_1 = time()
    print("Виконання рекурсією: \n", max_el_rec(x))
    ti_1 = time()
    rec_time = ti_1 - t_1
    t_2 = time()
    print("Виконання ітерацією: \n", max_el_iter(x))
    ti_2 = time()
    iter_time = ti_2 - t_2
    print()
    print(f"Час виконання:\n Ітерація = {iter_time}\n Рекурсія = {rec_time}")
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break
# Ітерація замає менше коду
# Ітерація виконується швидше.
# Рекурсія забирає більше пам'яті через зберігання значень у стеку.
# Ітерація більш читабелніша за рекурсію
