'''Создайте класс Player.
Поля:
- имя пользователя - user_name,
- использованные слова пользователя - is_using_words.
Методы:
- получение количества использованных слов (вернет int) - using_words,
- добавление слова в использованные слова (ничего не возвращает),
- проверка использования данного слова до этого (вернет bool)
- __repr__
'''


class Player:
    def __init__(self, user_name):
        self.user_name = user_name
        self.is_using_words = []

    def __repr__(self):
        return f"Player(user_name={self.user_name}, is_using_words={self.is_using_words})"

    def using_words(self):
        return len(self.is_using_words)

    def add_word(self, user_answer):
        self.is_using_words.append(user_answer)

    def is_correct_list(self, user_answer):
        return user_answer in self.is_using_words
