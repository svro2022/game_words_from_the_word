'''Создайте класс BasicWord.
Он будет содержать поля:
- исходное слово - original_word,
- набор допустимых подслов - is_correct_words.
Методы:
- проверка введенного слова (user_answer) в списке допустимых подслов (вернет True или False) - def is_correct(self)
- подсчет количества слов, вернет int (words_count)
- __repr__
'''

class BasicWord:
    def __init__(self, original_word, is_correct_words):
        self.original_word = original_word
        self.is_correct_words = is_correct_words

    def __repr__(self):
        return f"BasicWord(original_word={self.original_word}, is_correct_words={self.is_correct_words})"

    def is_correct(self, user_answer):
        return user_answer in self.is_correct_words

    def words_count(self):
        return len(self.is_correct_words)
