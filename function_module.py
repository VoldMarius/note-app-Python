from datetime import datetime

import pandas as pd


def record_data():
    title = input('Ведите заголовок(доп.инфо): \n')
    message = input('Ведите текст заметки: \n')

    df = pd.DataFrame([{
        'Тема': title,
        'Текст заметки': message,
        'Время': datetime.today()
    }])
    df.to_csv('notes.csv', mode='a', header=True, index=False)


def find_data():
    changes_vol = input(
        'для поиска -  введите  Дату записи в формате->YYYY-MM-DD')
    print('*' * 10)
    df = pd.read_csv('notes.csv')
    filtered_df = df[df['Время'].str.contains(changes_vol)]
    if len(filtered_df) == 0:
        print("Заметки с такой датой нет")
        exit()
    else:
        print(filtered_df)


def change_data():
    find_data()
    df = pd.read_csv('notes.csv')
    changes_vol = int(input('Введите индекс заметки для изменения:  '))
    title = input('Ведите заголовок(доп.инфо): \n')
    message = input('Ведите новый текст заметки: \n')
    print('*' * 10)

    df.iloc[changes_vol] = [title, message, datetime.today()]
    df.to_csv('notes.csv', index=False)