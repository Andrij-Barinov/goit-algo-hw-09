# Порівняння жадібного алгоритму та алгоритму динамічного програмування для видачі решти

## Вступ

Це завдання передбачає розробку двох різних підходів для вирішення задачі про розбиття суми на монети: жадібного алгоритму та динамічного програмування.

## Реалізація

- **Жадібний алгоритм**: Спочатку вибирає найбільші доступні номінали монет і намагається з їх допомогою сформувати необхідну суму.
- **Динамічне програмування**: Використовує таблицю для збереження мінімальної кількості монет для кожної суми від 0 до потрібної.

## Ефективність

### Жадібний алгоритм:

- **Часова складність**: O(n), де n — кількість номіналів монет.
- **Переваги**: Простий та швидкий у реалізації.
- **Недоліки**: Не завжди дає оптимальне рішення, якщо набір монет не дозволяє жадібному підходу працювати ефективно.

### Динамічне програмування:

- **Часова складність**: O(n \* m), де n — кількість номіналів монет, m — сума для розбиття.
- **Переваги**: Гарантує знаходження мінімальної кількості монет для будь-якого набору номіналів.
- **Недоліки**: Складніший у реалізації, може бути менш ефективним за часом для великих сум.

## Висновок

- Жадібний алгоритм підходить для швидкого вирішення, якщо набір монет дозволяє отримати оптимальне рішення.
- Алгоритм динамічного програмування є більш універсальним та гарантує мінімальну кількість монет, але може займати більше часу для великих сум.

В залежності від конкретного набору монет та суми, варто вибирати той чи інший підхід. Для касових апаратів, де набори монет відомі заздалегідь, жадібний алгоритм зазвичай працює достатньо добре. Однак, для більш загальних задач з довільними номіналами монет, динамічне програмування буде кращим вибором.
