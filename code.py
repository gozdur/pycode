


def hello_func(greeting, name='Pawel'):
    return '{}, {}'.format(greeting, name)

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

# output of function hello_func
xxx = 'Marek'
print(hello_func('Hi', xxx))

# output of function student_info

kursy = ['ccna', 'jncia']
nauczyciel = {'name': 'Adam', 'age': 22}

student_info('Math', 'Art', name='John', age=22)
student_info(*kursy, **nauczyciel)



