# Программа для учета расходов

# Инициализация переменной для хранения расходов
total_expenses = 0

# Запрос начальной даты периода
while True:
    start_date = input("Введите начальную дату периода (1-7): ")
    if start_date.isdigit() and 1 <= int(start_date) <= 7:
        start_date = int(start_date)
        break
    else:
        print("Неверный формат даты. Пожалуйста, введите число от 1 до 7.")

# Запрос конечной даты периода
while True:
    end_date = input("Введите конечную дату периода (1-7): ")
    if end_date.isdigit() and start_date <= int(end_date) <= 7:
        end_date = int(end_date)
        break
    else:
        print("Неверный формат даты или дата меньше начальной. Пожалуйста, введите число от 1 до 7.")

# Ввод расходов за указанный период
for day in range(start_date, end_date + 1):
    print("\n" + "=" * 50)
    print(f"{' День ' + str(day) + ' недели ':=^50}")
    print("=" * 50)
    
    daily_expense = float(input("Введите сумму расходов за день: "))
    total_expenses += daily_expense

# Красивый вывод общей суммы расходов за период
print("\n" + "=" * 50)
print(f"{' Общая сумма расходов за период ':<50} {total_expenses:>10.2f}")
print("=" * 50)
