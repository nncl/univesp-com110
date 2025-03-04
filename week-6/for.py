animals = ['dog', 'cat', 'cow', 'gorilla']

def print_animals(args: [str]) -> None:
    for item in args:
        print(item)

    for item in range(len(args)):
        print(item, args[item])

print_animals(animals)