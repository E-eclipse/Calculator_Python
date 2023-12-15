import pandas as pd
import numpy as np

pokemon = pd.read_csv('pokemon.csv')

# Вывести весь датасет и опишите его
print(pokemon)

print("\n================================")

# Вывести наименование всех колонок, написать что они означают в вашем датасете
for i in pokemon:
    print(i)

print("\n================================")

# Вывести размерноть массива
rows = len(pokemon.axes[0]) 
cols = len(pokemon.axes[1])
#! можно и через shape, но так не интересно
print(f"Строк:{rows}\nСтолбцов:{cols}")

print("\n================================")

# Вывести все уникальные значения
for i in pokemon:
    print(pokemon[i].unique())

print("\n================================")

# Отсортировать по определенным параметрам
pokemon = pokemon.sort_values(by="attack")
print(pokemon)

print("\n================================")

# Удалить ненужные столбцы или строчки 
pokemon = pokemon.drop(["type2"], axis = 1)
print(pokemon)

print("\n================================")

# Заменить определенные значения в датасете (например, пустые)
pokemon = pokemon.replace({"generation":2}, 5)

print(pokemon)
print("\n================================")

# Удалить дубликаты
pokemon.drop_duplicates()

# Провести анализ с помощью функций info
print(pokemon.info())
print("\n================================")

# Провести анализ с помощью функций describe
print(pokemon.describe(include='all'))
print("\n================================")

# Провести выборку данных по строкам и столбцам с помощью loc
Water_pokemon = pokemon.loc[pokemon["type1"] == "Water"]

print(Water_pokemon)
print("\n================================")


# Сохранить новый датасет
pokemon.to_csv("Pokemon.csv", index=False)