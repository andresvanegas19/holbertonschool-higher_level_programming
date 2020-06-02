#!/usr/bin/python3
""" a class that inherent from list"""


class MyList(list):
    """This classs inherent to list and
    carry whole atributes"""
    # ya heredo todas las funciones
    # de list entonces ya no es necesario
    # que haga append
    # __iter__ es una funcion que
    # itera sobre nuestra lista
    def print_sorted(self):
        """print the list of the inherent class
        in oreder"""
        print(sorted([a for a in super().__iter__()]))



