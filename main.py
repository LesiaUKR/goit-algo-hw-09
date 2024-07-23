import timeit  # Імпорт модуля timeit для вимірювання часу виконання функцій
from tabulate import tabulate  # Імпорт функції tabulate для виведення таблиць

coins = [50, 25, 10, 5, 2, 1]  # Набір доступних монет

# Функція жадібного алгоритму для видачі решти
def find_coins_greedy(amount):
    
    result = {}  # Словник для зберігання результатів

    for coin in coins:  # Перебір кожної монети
        if amount >= coin:  # Перевірка, чи можна використати цю монету
            result[coin] = amount // coin  # Додавання кількості монет цього номіналу
            amount = amount % coin  # Оновлення залишкової суми

    return result  # Повернення результату

# Функція динамічного програмування для видачі решти
def find_min_coins(amount):
   
    min_coins = [0] + [float('inf')] * amount  # Ініціалізація списку мінімальної кількості монет для кожної суми
    coin_count = [{} for _ in range(amount + 1)]  # Список для зберігання словників з кількістю монет для кожної суми

    for coin in coins:  # Перебір кожної монети
        for x in range(coin, amount + 1):  # Перебір кожної суми від номіналу монети до заданої суми
            if min_coins[x - coin] + 1 < min_coins[x]:  # Перевірка, чи можна зменшити кількість монет
                min_coins[x] = min_coins[x - coin] + 1  # Оновлення мінімальної кількості монет для суми x
                coin_count[x] = coin_count[x - coin].copy()  # Копіювання словника з кількістю монет для суми x - coin
                if coin in coin_count[x]:  # Перевірка, чи монета вже використовується
                    coin_count[x][coin] += 1  # Збільшення кількості монет цього номіналу
                else:
                    coin_count[x][coin] = 1  # Додавання нової монети до словника

    return coin_count[amount]  # Повернення результату для заданої суми

# Визначення різних значень суми для видачі решти
amounts = [10, 55, 113, 207, 505, 1001]  # Суми, для яких будемо проводити вимірювання

# Збирання результатів вимірювання часу виконання
results = []  # Список для зберігання результатів

for amount in amounts:  # Перебір кожної суми
    time_greedy = timeit.timeit(lambda: find_coins_greedy(amount), number=1000)  # Вимірювання часу виконання жадібного алгоритму
    time_dp = timeit.timeit(lambda: find_min_coins(amount), number=1000)  # Вимірювання часу виконання алгоритму динамічного програмування
    results.append([amount, time_greedy, time_dp])  # Додавання результатів до списку

# Виведення результатів у вигляді таблиці
headers = ["Amount", "Функція жадібного алгоритму (s)", "Функція динамічного програмування (s)"]  # Заголовки таблиці
table = tabulate(results, headers, tablefmt="pipe")  # Формування таблиці з результатами
print(table)  # Виведення таблиці

