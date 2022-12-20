# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import pathlib
from pathlib import Path

enter_path = Path("Homework", "Homework5", "data.txt")
result_path = Path("Homework", "Homework5", "result.txt")

with open(enter_path, "r", encoding = 'utf-8') as data:
    a = data.read()

res = " ".join([item for item in a.split() if "абв" not in item])

with open(result_path, "a", encoding = 'utf-8') as data:
    data.write(res)
