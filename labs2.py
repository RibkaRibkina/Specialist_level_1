# Игра “Поле чудес”
import random


while True:
    word = ["книга", "месяц", "ручка", "шарик", "олень", "носок", "телевизор"]
    word_game = random.choice(word)
    curent_view = []
    for i in range(0, len(word_game)):
        curent_view.append("\u25A0")
    game_on = input("Хотите сыграть (Да/Нет): ")
    if game_on == "Да" or game_on == "да":
        counter_life = int(input("Выберите количество жизне: "))
        while counter_life > 0:
            print(" ".join(curent_view), "|" f" Жизни х {counter_life}")
            answer = input("Назовите букву или слово целиком: ")
            if answer == word_game:
                print("Поздравляем Вы выиграли!")
                break
            elif answer in word_game:
                for i in range(0, len(word_game)):
                    if word_game[i] == answer:
                        curent_view[i] = answer
            else:
                print("Нет такой буквы!!!")
                counter_life -= 1
            if "".join(curent_view) == word_game:
                print("Поздравляем Вы угадали слово!!!")
                break
            if counter_life == 0:
                print("Вы проиграли!!!")
    else:
        print("Досвидания!")
        break
