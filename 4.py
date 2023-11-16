import time
import random
from collections import deque

# Генеруємо випадкові дані для списку
N = 100000
data = [random.randint(0, N) for _ in range(N)]

# Кількість елементів для вставки
insert_count = 1000

# Заповнення ArrayList
start = time.time()
array_list = list(data)
end = time.time()
fill_array_list = end - start

# Заповнення LinkedList
start = time.time()
linked_list = deque(data)
end = time.time()
fill_linked_list = end - start

# Доступ за випадковому індексу
index = random.randint(0, N-1)

start = time.time()
element_array = array_list[index]
end = time.time()
index_array = end - start

start = time.time()
element_linked = linked_list[index]
end = time.time()
index_linked = end - start

# Доступ за ітератором (Sequential Access)
start = time.time()
for element in array_list:
    pass
end = time.time()
seq_access_array = end - start

start = time.time()
for element in linked_list:
    pass
end = time.time()
seq_access_linked = end - start

# Вставка елементу на початок списку
start = time.time()
for i in range(insert_count):
    array_list.insert(0, random.randint(0, N))
end = time.time()
insert_array_start = end - start

start = time.time()
for i in range(insert_count):
    linked_list.appendleft(random.randint(0, N))
end = time.time()
insert_linked_start = end - start

# Вставка елементу в кінець списку
start = time.time()
for i in range(insert_count):
    array_list.append(random.randint(0, N))
end = time.time()
insert_array_end = end - start

start = time.time()
for i in range(insert_count):
    linked_list.append(random.randint(0, N))
end = time.time()
insert_linked_end = end - start

# Вставка елементу в середину списку
start = time.time()
for i in range(insert_count):
    array_list.insert(len(array_list) // 2, random.randint(0, N))
end = time.time()
insert_array_middle = end - start

start = time.time()
for i in range(insert_count):
    linked_list.insert(len(linked_list) // 2, random.randint(0, N))
end = time.time()
insert_linked_middle = end - start

# Виведення результатів
print(f"Час заповнення ArrayList: {fill_array_list}")
print(f"Час заповнення LinkedList: {fill_linked_list}")
print(f"Час доступу за індексом у ArrayList: {index_array}")
print(f"Час доступу за індексом у LinkedList: {index_linked}")
print(f"Час послідовного доступу у ArrayList: {seq_access_array}")
print(f"Час послідовного доступу у LinkedList: {seq_access_linked}")
print(f"Час вставки в початок ArrayList: {insert_array_start}")
print(f"Час вставки в початок LinkedList: {insert_linked_start}")
print(f"Час вставки в кінець ArrayList: {insert_array_end}")
print(f"Час вставки в кінець LinkedList: {insert_linked_end}")
print(f"Час вставки в середину ArrayList: {insert_array_middle}")
print(f"Час вставки в середину LinkedList: {insert_linked_middle}")
