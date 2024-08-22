def find_coins_greedy(amount):
    # Список доступних номіналів монет у порядку спадання
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    # Жадібний підхід: спочатку використовуємо найбільші можливі монети
    for coin in coins:
        if amount >= coin:
            # Додаємо до словника кількість монет даного номіналу
            result[coin] = amount // coin
            # Оновлюємо суму, віднявши вже використані монети
            amount = amount % coin
    
    # Повертаємо словник із кількістю використаних монет кожного номіналу
    return result

def find_min_coins(amount):
    # Список доступних номіналів монет у порядку зростання
    coins = [1, 2, 5, 10, 25, 50]
    # Ініціалізуємо масив для збереження мінімальної кількості монет для кожної суми
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # Нуль монет потрібен для суми 0
    # Масив для збереження останньої монети, що використовувалась для досягнення певної суми
    coin_used = [0] * (amount + 1)
    
    # Перебираємо всі можливі суми від 1 до заданої
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                # Перевіряємо, чи використання цієї монети призведе до меншої кількості монет
                if min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1
                    coin_used[i] = coin  # Зберігаємо монету, що використовується
    
    # Формуємо результат у вигляді словника
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin  # Зменшуємо суму на величину монети
    
    # Повертаємо словник із кількістю використаних монет кожного номіналу
    return result

# Тести
if __name__ == "__main__":
    # Тести для жадібного алгоритму
    print("Жадібний алгоритм для суми 113:", find_coins_greedy(113))  # {50: 2, 10: 1, 2: 1, 1: 1}
    print("Жадібний алгоритм для суми 78:", find_coins_greedy(78))    # {50: 1, 25: 1, 2: 1, 1: 1}

    # Тести для динамічного програмування
    print("Динамічне програмування для суми 113:", find_min_coins(113))  # {50: 2, 10: 1, 2: 1, 1: 1}
    print("Динамічне програмування для суми 78:", find_min_coins(78))    # {50: 1, 25: 1, 2: 1, 1: 1}
