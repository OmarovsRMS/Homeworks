tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]


def func_gen(list1, list2):
    while len(list1) > len(list2):
        list2.append(None)

    for i in range(len(list1)):
        yield (list1[i], list2[i])

my_gen = func_gen(tutors, klasses)

print(my_gen)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

