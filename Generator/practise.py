def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up_to(3)

for num in gen:
    print(num)

# def creator():
#     i = 1
#     while i <= 200:
#      yield i
#      i += 1
# print(creator())
# x = creator()
# print(next(x))
# print(next(x))
# print(list(x))

# def creator():
# This defines a generator function named creator.

# yield i
# Instead of returning a value and stopping, yield produces a value and pauses the function, saving its state so it can resume from that point later. This makes it a generator.

# print(creator())
# This prints the generator object itself, like: <generator object creator at 0x...>, not the actual values.

# x = creator()
# This creates a generator object and assigns it to x.

# print(next(x))
# This resumes the generator and returns the first value: 1.

# print(next(x))
# Continues the generator and returns the next value: 2.

# print(list(x))
# Converts the rest of the generator (from current state) to a list. Since we've already consumed 1 and 2, it prints [3, 4, ..., 200].