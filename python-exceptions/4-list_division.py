#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    chaima = []
    for i in range(0, list_length):
        try:
            chouchou = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            chouchou = 0
        except ZeroDivisionError:
            print("division by 0")
            chouchou = 0
        except IndexError:
            print("out of range")
            chouchou = 0
        except Exception as e:
            pass
        finally:
            chaima.append(chouchou)
    return (chaima)
