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
    df.to_csv('notes.csv', mode='a', header=False, index=False)


def find_data():
    changes_vol = input(
        'введите  Дату записи в формате -> YYYY-MM-DD :   ')
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


def delete_data():
    find_data()
    df = pd.read_csv('notes.csv')
    changes_vol = int(input('Введите индекс заметки для удаления:  '))
    print('*' * 10)
    df = df.drop(index=changes_vol, axis=0)


def show_list():
    df = pd.read_csv('notes.csv')
    print('*' * 20)
    print(df)
    print('*' * 30)


def show_notes_by_topic():
    df = pd.read_csv('notes.csv')
    print(df['Тема'].unique())
    changes_vol = str(input(
        'для просмотра введите Тему из списка '))
    print('*' * 10)
    filtered_df = df[df['Тема'].str.contains(changes_vol)]
    if len(filtered_df) == 0:
        print("Заметки с такой датой нет")
        exit()
    else:
        print(filtered_df)
