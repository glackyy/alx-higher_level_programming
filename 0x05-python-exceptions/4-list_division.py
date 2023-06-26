#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for i in range(list_length):
        try:
            e1 = my_list_1[i]
            e2 = my_list_2[i]
            if isinstance(e1, (int, float)) and isinstance(e2, (int, float)):
                if e2 == 0:
                    raise ZeroDivisionError
                res = e1 / e2
            else:
                 raise TypeError
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except TypeError:
            print("wrong type")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            n_list.append(res)
    return n_list
