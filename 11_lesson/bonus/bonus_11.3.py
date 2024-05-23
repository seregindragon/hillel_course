def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Повертає індекс знайденого елемента

    return -1  # Повертає -1, якщо елемент не знайдено


# Перевірка
assert linear_search([64, 34, 25, 12, 22, 11, 90], 22) == 4
