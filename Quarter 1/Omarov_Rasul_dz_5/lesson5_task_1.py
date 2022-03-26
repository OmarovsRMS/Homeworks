def odd_nums(num):
    for i in range(num+1):
        if i % 2!=0:
            yield i


gen_nums = odd_nums(11)

print(next(gen_nums))
print(next(gen_nums))
print(next(gen_nums))
print(next(gen_nums))
print(next(gen_nums))
print(next(gen_nums))
print(next(gen_nums))

