from config import WORKING_DIR
from file_manager import FileManager

def display_help():
    """Выводит справку по всем доступным командам."""
    print("""
Доступные команды:

  Навигация:
    cd <path>       - Перейти в указанную директорию.
    ls              - Показать содержимое текущей директории.

  Работа с директориями:
    mkdir <name>    - Создать новую директорию.
    rmdir <name>    - Удалить пустую директорию.

  Работа с файлами:
    touch <name>    - Создать новый файл.
    rm <name>       - Удалить файл.
    read <name>     - Прочитать содержимое файла.
    write <name>    - Записать данные в файл.

  Дополнительные операции:
    copy <src> <dst> - Скопировать файл или директорию.
    move <src> <dst> - Переместить файл или директорию.
    rename <old> <new> - Переименовать файл или директорию.

  Справка и выход:
    help            - Показать эту справку.
    exit            - Завершить работу программы.
""")

def main():
    # Инициализация файлового менеджера с рабочей директорией из config.py
    manager = FileManager(WORKING_DIR)

    # Вывод приветственного сообщения
    print("Добро пожаловать в файловый менеджер!")
    print("Напишите 'help', чтобы вывести справку.\n")

    while True:
        command = input(f"{manager.current_dir}> ").strip()
        if not command:
            continue

        parts = command.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd == "cd":
            if len(args) != 1:
                print("Использование: cd <путь>")
            else:
                manager.change_directory(args[0])
        elif cmd == "ls":
            manager.list_directory()
        elif cmd == "mkdir":
            if len(args) != 1:
                print("Использование: mkdir <имя>")
            else:
                manager.create_directory(args[0])
        elif cmd == "rmdir":
            if len(args) != 1:
                print("Использование: rmdir <имя>")
            else:
                manager.remove_directory(args[0])
        elif cmd == "touch":
            if len(args) != 1:
                print("Использование: touch <имя>")
            else:
                manager.create_file(args[0])
        elif cmd == "rm":
            if len(args) != 1:
                print("Использование: rm <имя>")
            else:
                manager.delete_file(args[0])
        elif cmd == "read":
            if len(args) != 1:
                print("Использование: read <имя>")
            else:
                manager.read_file(args[0])
        elif cmd == "write":
            if len(args) != 1:
                print("Использование: write <имя>")
            else:
                manager.write_file(args[0])
        elif cmd == "copy":
            if len(args) != 2:
                print("Использование: copy <источник> <назначение>")
            else:
                manager.copy_item(args[0], args[1])
        elif cmd == "move":
            if len(args) != 2:
                print("Использование: move <источник> <назначение>")
            else:
                manager.move_item(args[0], args[1])
        elif cmd == "rename":
            if len(args) != 2:
                print("Использование: rename <старое_имя> <новое_имя>")
            else:
                manager.rename_item(args[0], args[1])
        elif cmd == "help":
            display_help()
        elif cmd == "exit":
            print("Выход из программы.")
            break
        else:
            print("Неизвестная команда. Введите 'help' для просмотра списка команд.")

if __name__ == "__main__":
    main()
