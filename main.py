invalid_names = ["hello", "world"]

def get_index_by_name(name):
    return invalid_names.index(name)

print(get_index_by_name("hello"))
print(get_index_by_name("world"))
