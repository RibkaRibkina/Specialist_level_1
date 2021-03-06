# Парадокс Монти Холла
# Парадокс Монти Холла — одна из известных задач теории вероятностей, решение
# которой, на первый взгляд, противоречит здравому смыслу.
# Парадокс основан на американском телешоу «Let's Make a Deal» и назван в честь
# ведущего этой передачи.
# Правила игры
# Участнику игры нужно выбрать одну из трёх дверей. За одной из дверей находится приз,
# за двумя другими дверями ничего нет. Участнику выбирает одну из дверей, например,
# номер 1, после этого ведущий, который знает, где находится приз, открывает одну из
# оставшихся дверей, например, номер 3, за которой ничего нет. После этого он спрашивает
# участника: не желаете ли он изменить свой выбор и выбрать дверь номер 2? Участник
# может согласиться либо остаться при своём выборе.
# Вопрос
# Увеличиваются ли шансы участника выиграть приз, если он примет предложение
# ведущего и измените свой выбор?
# Предположения
# ● Математики утверждают, что увеличатся на 60%.
# ● Разум подсказывает, что нет.
# Задание
# Напишите программу, которая подтвердит или опровергнет доводы математиков.
# Помощь
# Для решения задачи вам потребуется импортировать модуль random:
# import random
# и использовать его метод randrange. Метод randrange принимает в качестве аргумента
# два числа n1 и n2 и генерирует случайное число в диапазоне от n1 до n2-1:
# random.randrange(2, 5)
# вернёт либо 2, либо 3, либо 4

import random

counter = 0
counter_lose = 0
while counter < 10000:
    counter += 1
    door = random.randrange(1, 4)
    print(f"Выигрыш за дверью {door}")
    answer = random.randrange(1, 4)
    print(f"Робот выбрал дверь {answer}")
    if door == answer:
        counter_lose += 1
print(f"Процент побед : {(10000 - counter_lose) / 100}")
