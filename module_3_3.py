

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(2,4)
print_params('a', 'b', 'c')


values_list = ('mother', False, 1024)
values_dict = {'a' : 3.25, 'b': 'Programm', 'c': False}
print_params(*values_list)
print(values_dict)
print_params(*values_dict)
print_params(**values_dict)


values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)