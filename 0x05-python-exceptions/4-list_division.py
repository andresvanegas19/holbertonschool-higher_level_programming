#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    number = 0
    for num in range(list_length):
        try:
            my_list_1[num] / my_list_2[num]
        except (ValueError, TypeError):
            print('wrong type')
            number = 0
        except ZeroDivisionError:
            print('division by 0')
            number = 0
        except IndexError:
            print('out of range')
            number = 0
        else:
            number = my_list_1[num] / my_list_2[num]
        finally:
            new_list.append(number)
    return new_list
