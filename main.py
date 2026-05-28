import tools as s
path = "tasks.json"
tasks = s.open_json(path)
while True:
    s.menu()
    try:
        num = int(input("Введите число для выбора:"))
        if num == 1:
            s.show_tasks(tasks)
            tasks = s.open_json(path)
        if num == 2:
            s.add_task(path, tasks)
            tasks = s.open_json(path)
        if num == 3:
            s.complete_task(path, tasks)
            tasks = s.open_json(path)
        if num == 4:
            s.delete_task(path, tasks)
            tasks = s.open_json(path)
        if num == 5:
            s.search_task(tasks)
            tasks = s.open_json(path)
        if num == 6:
            break



    except ValueError:
        print("Введите число")


