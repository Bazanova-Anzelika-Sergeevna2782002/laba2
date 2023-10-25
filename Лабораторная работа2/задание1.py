money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
mounth = 0
remainder = money_capital + salary
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while spend <= remainder:
    lesion = spend - salary
    money_capital -= lesion
    remainder = money_capital + salary
    spends = spend * increase
    spend += spends
    mounth += 1
print("Количество месяцев, которое можно протянуть без долгов:", mounth)
