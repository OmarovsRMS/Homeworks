def thesaurus(*args):
    my_dict = {}
    for name in args:
        my_sort = list(filter(lambda x: x.startswith(name[0]), args))
        my_dict.update({name[0]: my_sort})
    print(my_dict)

thesaurus('Иван','Никифор','Петр','Игорь','Мария','Николай')
