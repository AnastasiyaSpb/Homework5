# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import pathlib
from pathlib import Path


def rle_do(data):
    result = ""
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count = count + 1
            i += 1
        result += str(count) + data[i]
        i += 1
    return result


def rle_back(data):
    result = ""
    i = 0
    while i < len(data):
        if data[i].isnumeric():
            result += data[i+1] * (int(data[i]) -1)
            i += 1
        else:
            result += data[i]
            i += 1
    return result


enter_path = Path("Homework", "Homework5", "enter_data.txt")
result_path = Path("Homework", "Homework5", "result_data.txt")

# with open(enter_path, "r", encoding='utf-8') as data:
#     a = data.read()

# res = rle_do(a)

# with open(result_path, "a", encoding='utf-8') as data:
#     data.write(res)

with open(result_path, "r", encoding='utf-8') as data:
    a = data.read()

res = rle_back(a)

with open(enter_path, "a", encoding='utf-8') as data:
    data.write(res)
