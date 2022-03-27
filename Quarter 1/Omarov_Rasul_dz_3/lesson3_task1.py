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


def num_translate(value):
    if value in my_dict.keys():
        return my_dict[value]
    else:
        return None


print('Числительное на русском языке: ', num_translate(eng_num))

