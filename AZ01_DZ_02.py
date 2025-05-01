import pandas as pd

# Загрузка данных из CSV-файла в DataFrame
df = pd.read_csv('dz.csv')

# Преобразование Salary в числовой формат и замена пропусков на NaN
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

# Расчет средней зарплаты по городам
average_salary_by_city = df.groupby('City')['Salary'].mean().reset_index()

# Вывод результата
print("Средняя зарплата по городам:")
print(average_salary_by_city)

# print("значения до целых чисел")
# average_salary_by_city['Salary'] = average_salary_by_city['Salary'].round()
# print(average_salary_by_city)
