from controler_data import operation_function


def dialog_values():
    incoming_vol = int(input(
        'Выбереите:\n'
        '1 - для создания записи \n'
        '2 - для поиска записи \n'
        '3 - для внесения изменений \n'
        '4 - для выхода \n '
        '******** \n'
        '==>  '))
    if incoming_vol is not None:
        while incoming_vol < 4:
            if incoming_vol == 1:
                return incoming_vol
            elif incoming_vol == 2:
                return incoming_vol
            elif incoming_vol == 3:
                return incoming_vol
            else:
                print('Ошибка ввода!')
    else:
        print('Ошибка ввода!')


operation_function(dialog_values())
