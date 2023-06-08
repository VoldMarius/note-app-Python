from controler_data import operation_function


def dialog_values():
    incoming_vol = input(
        'Выбереите:\n'
        '1 - для создания записи \n'
        '2 - для поиска записи по дате создания \n'
        '3 - для внесения изменений в запись \n'
        '4 - для удаления записи \n'
        '5 - для просмотра всего списка записей \n'
        '6 - для просмотра списка записей по Теме \n'
        '******** \n'
        '==>  ')

    if not incoming_vol:
        print("Вы ничего не ввели.")
    else:
        incoming_vol = int(incoming_vol)

        if incoming_vol == 1:
            return incoming_vol
        elif incoming_vol == 2:
            return incoming_vol
        elif incoming_vol == 3:
            return incoming_vol
        elif incoming_vol == 4:
            return incoming_vol
        elif incoming_vol == 5:
            return incoming_vol
        elif incoming_vol == 6:
            return incoming_vol
        else:
            print('Ошибка ввода!')


operation_function(dialog_values())
