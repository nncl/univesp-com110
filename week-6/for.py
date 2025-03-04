animals = ['dog', 'cat', 'cow', 'gorilla']

def print_animals(args: [str]) -> None:
    for item in args:
        print(item)

    for item in range(len(args)):
        print(item, args[item])

print_animals(animals)

def factorial(limit: int) -> int:
    count = 0
    fat = 1

    while fat <= limit:
        count += 1
        fat *= count
        print(count, fat, limit)

    return count - 1

print(factorial(20))