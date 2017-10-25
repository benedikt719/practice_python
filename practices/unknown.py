from random import shuffle

def num(number) :

    return [x for x in number if x < 0 ] + [y for y in number if y > 0]


large_a = list( [x for x in range(100) if x % 2 == 0 or x % 7 == 0] + [-x for x in range(100) if x % 3 == 0 or x % 5 == 0])

shuffle(large_a)

print(large_a)
print(num(large_a))




