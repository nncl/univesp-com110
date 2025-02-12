def get_index_by_name(name):
    invalid_names = ["hello", "world"]
    return invalid_names.index(name)

print(get_index_by_name("hello"))
print(get_index_by_name("world"))

def display_list_items():
    list_example = ['Conceito Tuplas', 'Fazer exercício 3', 345, ['rever slide 6', 334]]

    print(list_example[0])

    print(list_example)

    list_example[0] = 45

    print(list_example)

display_list_items()

def return_types():
    letter_1 = 'A',

    letter_2 = ('A', 'B')

    letter_3 = 'A'

    letter_4 = ('A')

    print(type(letter_1))

    print(type(letter_2))

    print(type(letter_3))

    print(type(letter_4))

return_types()

print('Type is', type('A'))
print('Type is', type(('A')))
print('Type is', type(('A', 'B')))

def return_name_by_index(index: int):
    names = ['João', 'Maria', 'José', 'Marta']
    print(names[index])

return_name_by_index(-1)

def update_first_grade():
    grades = [8.0, 5.5, 9.3, 7.6, 3.1]
    grades[0]=grades[0]+0.5
    print(grades)

update_first_grade()

def validate_data_types():
    print(type(5))
    print(type(3.2))
    print(type(['hello', 'world']))

validate_data_types()