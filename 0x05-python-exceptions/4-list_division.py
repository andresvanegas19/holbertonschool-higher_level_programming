#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for num in range(list_length):
        try:
            my_list_1[num] / my_list_2[num]
        except ValueError:
            print('wrong type')
            new_list.append(0)
        except ZeroDivisionError:
            print('division by 0')
            new_list.append(0)
        except IndexError:


