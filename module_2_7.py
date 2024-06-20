def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(31, 'String', False)
print_params(156, '25')
print_params(249)
print_params()


# Вызов с переопределением работает, но нам указывают на некорректность введённых данных
print_params(b=25)
print_params(c=[1, 2, 3])


values_list = [False, 33, "Timur"]
values_dict = {'a': "TEST", 'b': True, 'c': 86}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ["Age", 30]
print_params(*values_list_2, 42)  # Работает
