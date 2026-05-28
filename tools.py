import json
from json import JSONDecodeError


def menu():
    print("1 — показать все записи\n2 — добавить запись\n3 — отметить выполненной\n4 — удалить запись\n5 — поиск\n6 — выход")
def open_json(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            text = json.load(file)
        return text
    except (FileNotFoundError, JSONDecodeError):
        return []
def save_tasks(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
def show_tasks(tasks):
    if not tasks:
        print("Список пуст")
    else:
        for task in tasks:
            id_task = task["id"]
            if task["done"]:
                status = "[x]"
            else:
                status = "[ ]"
            title = task["title"]
            print(f"{id_task}. {status} {title}")
def add_task(path, tasks):
    note = input("Введите задачу:")
    if tasks:
        id_note = tasks[-1]["id"]+1
        tasks.append({"id": id_note, "title": note, "done": False})
        save_tasks(path, tasks)
    else:
        tasks.append({"id":1, "title": note, "done": False})
        save_tasks(path, tasks)
    print("успешно")
def complete_task(path, tasks):
    try:
        id_changed_task = int(input("Введите индекс задачи, которую вы хотите выполнить:"))
        if tasks:
            try:
                tasks[id_changed_task-1]["done"] = True
                save_tasks(path, tasks)
                print("успешно")
            except IndexError:
                print("Запись с таким id не найдена.")
        else:
            print("Список пуст")
    except ValueError:
        print("Неправильный тип данных")
def delete_task(path, tasks):
    try:
        id_deleted_task = int(input("Введите индекс задачи, которую вы хотите удалить:"))
        if tasks:
            try:
                del tasks[id_deleted_task-1]
                for task in tasks:
                    if id_deleted_task < task["id"]:
                        task["id"] -= 1
                save_tasks(path, tasks)
                print("успешно")
            except IndexError:
                print("Запись с таким id не найдена.")
        else:
            print("Список пуст")
    except ValueError:
        print("Неправильный тип данных")
def search_task(tasks):
    part = input("Введите часть задачи, которую вы хотите найти:")
    if tasks:
        for task in tasks:
            if part.lower() in task["title"].lower():
                if task["done"]:
                    status = "[x]"
                else:
                    status = "[ ]"
                print(task["id"] ,".", status, task["title"])
    else:
        print("Список пуст")
        print()