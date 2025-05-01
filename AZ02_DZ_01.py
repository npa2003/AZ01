import pandas as pd

# Создаем DF с данными об оценках
data = {
    'Ученик': ['Иванов', 'Петров', 'Сидоров', 'Назаров', 'Назарова',
               'Васильева', 'Попов', 'Новикова', 'Федоров', 'Морозова'],
    'Математика': [5, 4, 3, 5, 5, 3, 4, 5, 4, 3],
    'Физика': [4, 3, 4, 5, 5, 4, 4, 5, 3, 4],
    'Химия': [3, 4, 5, 5, 5, 5, 3, 4, 5, 3],
    'Литература': [4, 5, 4, 5, 5, 4, 5, 4, 3, 5],
    'История': [5, 4, 5, 5, 5, 5, 4, 5, 4, 3]
}

df = pd.DataFrame(data)

# первые строки DF
print("Первые 5 строк данных:")
print(df.head())

# средняя оценка по каждому предмету
mean_grades = df.mean(numeric_only=True)
print("\nСредняя оценка по предметам:")
print(mean_grades)

# медианная оценка
median_grades = df.median(numeric_only=True)
print("\nМедианная оценка по предметам:")
print(median_grades)

# Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print("\nСтатистика по математике:")
print(f"Q1 (25-й перцентиль): {Q1_math}")
print(f"Q3 (75-й перцентиль): {Q3_math}")
print(f"IQR (интерквартильный размах): {IQR_math}")

# стандартное отклонение
std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по предметам:")
print(std_deviation)