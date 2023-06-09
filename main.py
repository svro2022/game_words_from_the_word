from utils import load_random_word
from player_class import Player

load_word = load_random_word()

print(f"Введите имя игрока")
user_name = input('Ваш ответ: ')
player = Player(user_name)
print(f"Привет {player.user_name}!")
print(f"Составьте {len(load_word.is_correct_words)} слов из слова {load_word.original_word}")
print(f"Слова должны быть не короче 3 букв")
print(f"Чтобы закончить игру, угадайте все слова или напишите stop")
print(f"Поехали, Ваше первое слово?")

while player.using_words() < load_word.words_count():
    user_answer = input('Ваш ответ: ').lower()

    if len(user_answer) < 3:
        print(f"Слишком короткое слово.")

    elif user_answer in ['stop', 'стоп']:
        break

    elif player.is_correct_list(user_answer):
        print(f"Уже использовано")

    elif not load_word.is_correct(user_answer):
        print("Неверно")

    else:
        print("Верно")
        player.add_word(user_answer)


print(f"Игра завершена, Вы угадали {player.using_words()} слов!")
