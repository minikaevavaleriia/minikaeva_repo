def unique_symbols(s):
    list_ = []
    for i in s:
        list_.append(i)
    return len(set(list_))

print(unique_symbols('acjkgKKKKKKKKK'))