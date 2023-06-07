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
    # columns = df.columns
    # print(columns)
    if 'Время' not in df.columns:
        print("Столбец 'Время' не найден в DataFrame")

        exit()
    filtered_df = df[df['Время'].str.contains(changes_vol)]
    print(filtered_df)

