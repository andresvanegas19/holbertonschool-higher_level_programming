def get_function_mul(num):
    def multi(value):
        return num * value

    return multi


def div(num):
    return num / 2


save_func = get_function_mul(5)

print("{}".format(save_func(10)))

list_functions = [div, get_function_mul]

print(list_functions[0](10))

# dict is for dictionary

print(dir(dict))

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1, 7)))
# round necesita dos argumento, circle y range son sus argumentos
# map lo que hace es iterar sobre cada elemento
# circle_areas son los numeros y que se itera por cada numero y range es el numero de decimales
# el numero de decimales se va ir mostrando mientras itere el numero de range
# entonces map puede iterar varias variables al tiempo, pero si alguna de las listas que
# esta iterando se detiene, no va mas alla y la funcion para


#numeros = lambda x: x + x
# es mejor no usar lambda, en vez de eso usar
# usar una funcion normal, las lambda se usan cuando no la vamos utilizar mas de una vez
c = map(lambda x: x + x, filter(lambda x: (x >= 3), (1, 2, 3, 4)))

print(list(c))

# Dictionary with three keys
Dictionary1 = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}

# Printing keys of dictionary
print(Dictionary1.keys())
