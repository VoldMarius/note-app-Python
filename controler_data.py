from function_module import record_data, find_data, change_data, delete_data, show_list, show_notes_by_topic


def operation_function(data):

    if data == 1:
        return record_data()

    elif data == 2:
        return find_data()

    elif data == 3:
        return change_data()

    elif data == 4:
        return delete_data()

    elif data == 5:
        return show_list()
    elif data == 6:
        return show_notes_by_topic()
    else:
        print('Не верный ввод!')
