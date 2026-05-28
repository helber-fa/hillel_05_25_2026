# ctrl + / - одинарний коментар
# ctrl + alt + L - форматувати код

# snake_case - іменування змінних
# CamelCase - іменування класів
# UPPER_SNAKE - з великої літери, _ між словами

# = - оператор присвоєння
# == - оператор порівняння, повертає True/False

print("Hello world!")

my_int = 10
another_int = 20
another_int = my_int
# для примітивних типів, рівні значення означають що об'єкти посилаються на одну і ту ж комірку пам'яті
print(id(my_int))
print(id(another_int))

my_float = 15.3
# функція що виводить дип змінної
print(type(my_float))

# декілька обчислень можна записати одним рядком
my_sum = int(my_int + my_float)
# або ж в декілька
my_sum = my_int + my_float
my_sum = int(my_sum)
# результат такий самий
print(my_sum)

# рядок
my_string = "Hello"

# список
my_list = [1, 2, 5.9, True, [1, 0], ]

# тупл
my_tuple = (1, 2, None)

# сет
my_set = {1, 2, False}

# словник
my_dict = {"key": "value", "key2": {"sub_key": "sub_value"}}

# булева змінна
my_bool = True

my_none = None

# my_variable = None
# print(my_variable)
# my_variable = my_int + my_float
# print(my_variable)

# константа в Python - загальноприйнята умовність
MY_VARIABLE = 10
print(MY_VARIABLE)
MY_VARIABLE = "Hello"
print(MY_VARIABLE)

_ = "Trash variable"

BASE_PAGE_URL = "google.com"

# базові операції
sum_ = 10 + 10
diff = 15 - 10
mult = 5 * 12
div = 50 / 5

# фунція знаходження суми
sum([1, 2, 3])

print(sum_)
print(diff)
print(mult)
print(div)


# багаторядковий коментар, немає значення використовувати одинарні чи подвійні лапки
'''
if sum_ == 15:
    print("sum is equal to 15")
    if div == 0:
        print("zero divination")
'''

# одночасне присвоєння декількох змінних
my_name, my_age = "Alex", 30
copy_age, copy_name = my_age, my_name
print("Hello my name is", my_name, "My age is", my_age)
print(copy_name, copy_age)

# функція print приймає безліч аргументів, перетворює їх всі у рядки і виводить з розділювачем вказаним у аргументі sep
print("Hello", my_name, end="",sep="+")







