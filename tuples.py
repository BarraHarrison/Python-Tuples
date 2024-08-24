import sys

my_tuple = tuple(["Max", 28, "Boston"])
print(my_tuple)

item = my_tuple[2]
print(item)

if "Max" in my_tuple:
    print("yes")
else:
    print("no")

name, age, city = my_tuple
print(name)
print(age)
print(city)

my_new_list = [0, 1, 2, "hello", True]
my_new_tuple = [0, 1, 3, "hello", True]
print(sys.getsizeof(my_new_list), "bytes")
print(sys.getsizeof(my_new_tuple), "bytes")
