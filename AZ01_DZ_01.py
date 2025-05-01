import pandas as pd

# Загрузка данных из CSV-файла в DataFrame

df = pd.read_csv('farm_production_dataset.csv')

# Вывод первых 5 строк данных
print("Первые 5 строк данных:")
print(df.head())

# Вывод информации о данных и статистического описания
print("\nИнформация о данных:")
print(df.info())

print("\nСтатистическое описание данных:")
print(df.describe())