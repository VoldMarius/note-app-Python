from datetime import date, time, datetime
import pandas as pd

df = pd.read_csv('names1.csv')

title = input('Ведите заголовок(доп.инфо): \n')
message = input('Ведите текст заметки: \n')

number = len(df)+1

df = pd.DataFrame({'Номер записи': number,
                   'Тема': title,
                   'Текст заметки': message,
                   'Время записи': datetime.today()
                   }, index=[0])
df.to_csv('names1.csv', mode='a', sep=';', index=False, header=False)
print(df)
