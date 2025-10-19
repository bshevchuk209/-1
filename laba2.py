my_list = [22, 55 , 34, 98, 21, 22, 10, 50, 71, 99,
'giss', 'kis', 'pis', 'dad', 'bodya', 'tiotia', 'kolaps', 'mircle', 'opsich', 'qwertikow']
int_list = []
str_list = []
for x in my_list:
    if type(x) == int:
        int_list.append(x)
    else:
        str_list.append(x)
int_list.sort()
str_list.sort()

sorted_list = int_list.copy()
sorted_list.extend(str_list)
even_list = [x for x in int_list if x % 2 == 0]
upper_str_list = [x.upper() for x in str_list]
print("Основний список:", my_list)
print("Відсортований список:", sorted_list)
print("Список парних чисел:",even_list)
print("Список рядків у верхньому регістрі:",upper_str_list)

