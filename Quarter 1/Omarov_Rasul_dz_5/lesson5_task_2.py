def odd_nums(number):
    gen_nums = (num for num in range(number+1) if num % 2 != 0)
    return gen_nums

my_nums = odd_nums(11)

print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))

