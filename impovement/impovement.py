"""Создание списка, кортежа, словаря через цикл"""

data_list = [i**2 for i in range(1, 11)]
data_tuple = (i+1 for i in range(1, 11))
data_dict = {f"data{i}": i**2 for i in range(1, 10)}

print(data_dict)
