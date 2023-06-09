import random
import requests
from basicword_class import BasicWord


def load_random_word():
    response = requests.get('https://jsonkeeper.com/b/69BK', verify=False)
    data = response.json()
    random_word = random.choice(data)
    basicword = BasicWord(random_word['word'], random_word['subwords'])

    return basicword
