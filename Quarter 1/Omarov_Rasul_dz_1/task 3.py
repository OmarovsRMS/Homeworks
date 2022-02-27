for percent in range(1, 101):
    if 10 < percent <= 14:
        print(percent, 'процентов')
    elif str(percent)[-1] == '1':
        print(percent, 'процент')
    elif str(percent)[-1] == '2' or str(percent)[-1] == '3' or str(percent)[-1] == '4':
        print(percent, 'процента')
    else:
        print(percent, 'процентов')
