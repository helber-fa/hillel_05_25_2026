string_seq = "Hello Alex"
list_seq = [0,2,3,5,7]
tuple_seq = (1,2,3)
dict_seq = {"name":"Alex", "age":30}

set_seq = {1,2,3,5,"Hi"}


print(string_seq[0:10:2]) #[start(including):end(excluding):step]
print(string_seq[0:10]) #[start(including):end(excluding)] step - default 1
print(string_seq[::2]) #можна задати тільки частину параметрів
print(string_seq[::-1]) #ітерація з кінця
print(list_seq[1:len(list_seq)])

# print(len(string_seq))
# print(len(list_seq))
# print(len(tuple_seq))
# print(len(dict_seq))
#
# # Можна визначити довжину
# print(len(set_seq))
#
# print(string_seq[0])
# print(string_seq[6])
# print(string_seq[len(string_seq)-1])
#
#
# print(string_seq[-2])
#
# print(list_seq[1])
# print(tuple_seq[0])

# Неможливо отримати елемент по індексу
# print(set_seq[1])
# Неможливо отримати елемент по індексу
# print(dict_seq[0])





