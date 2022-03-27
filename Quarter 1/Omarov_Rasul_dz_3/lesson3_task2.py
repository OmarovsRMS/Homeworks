my_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

eng_num = input('Введите числительное на английском языке: ')


def num_translate_adv(value):
    if value in my_dict.keys():
        return my_dict[value]
    if value.lower() in my_dict.keys():
        return my_dict[value.lower()].capitalize()
    else:
        return None


print('Числительное на русском языке: ', num_translate_adv(eng_num))

