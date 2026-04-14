import json
import os

FILE_NAME = "vocabulary.json"

if not os.path.exists(FILE_NAME):
    print("Файл vocabulary.json не найден!")
    print("Создай файл и положи его рядом со скриптом")
    exit()

with open(FILE_NAME, "r", encoding="utf-8") as file:
    vocab = json.load(file)


def search_by_key(word):
    word = word.lower()
    if word in vocab:
        print(f"Перевод: {vocab[word]}")
    else:
        print("Слово не найдено")


def search_by_value(value):
    value = value.lower()
    found = False

    for key, val in vocab.items():
        if value in val.lower():
            print(f"Слово: {key} → {val}")
            found = True

    if not found:
        print("Перевод не найден")


while True:
    print("\n Поиск по словарю")
    query = input("Введи слово или перевод (или 'exit'): ").lower()

    if query == "exit":
        print("Выход...")
        break

    if query in vocab:
        search_by_key(query)
    else:
        search_by_value(query)
