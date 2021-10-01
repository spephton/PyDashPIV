def join(*iterables, joiner):
    if not iterables:
        return
    yield from iterables[0]
    for iterable in iterables[1:]: # this is valid. if there's only one item in iterables the loop isn't taken
        yield joiner
        yield from iterable
        
print(list(join([1, 5],[9, 2], [0], joiner = 7)))

print(list(join([1], joiner = 7)))