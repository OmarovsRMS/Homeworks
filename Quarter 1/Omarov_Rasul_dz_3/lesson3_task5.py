import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
jokes = []


def num_translate(num, repeat=True):
    """Функция выводит num шуток из трех случайных слов, взятых из 3-х разных списков"""
    if repeat == False:
        for i in range(0, num):
            word1 = random.choice(nouns)
            word2 = random.choice(adverbs)
            word3 = random.choice(adjectives)
            jokes.append(word1 + ' ' + word2 + ' ' + word3)
            nouns.pop(nouns.index(word1))
            adverbs.pop(adverbs.index(word2))
            adjectives.pop(adjectives.index(word3))
    else:
        for i in range(0, num):
            jokes.append(random.choice(nouns) + ' ' + random.choice(adverbs) + ' ' + random.choice(adjectives))

    print(jokes)


num_translate(4)