import os
import shutil
from utils import is_within_working_dir

class FileManager:
    def __init__(self, working_dir):
        self.working_dir = os.path.abspath(working_dir)
        self.current_dir = self.working_dir

    def change_directory(self, path):
        """Изменение текущей директории."""
        new_path = os.path.abspath(os.path.join(self.current_dir, path))
        if not is_within_working_dir(self.working_dir, new_path):
            print("Ошибка: Выход за пределы рабочей директории.")
            return
        if os.path.isdir(new_path):
            self.current_dir = new_path
        else:
            print(f"Ошибка: Директория '{path}' не существует.")

    def list_directory(self):
        """Вывод содержимого текущей директории."""
        try:
            items = os.listdir(self.current_dir)
            for item in items:
                print(item)
        except Exception as e:
            print(f"Ошибка: {e}")

    def create_directory(self, name):
        """Создание новой директории."""
        dir_path = os.path.join(self.current_dir, name)
        if not is_within_working_dir(self.working_dir, dir_path):
            print("Ошибка: Выход за пределы рабочей директории.")
            return
        try:
            os.mkdir(dir_path)
            print(f"Директория '{name}' создана.")
        except Exception as e:
            print(f"Ошибка: {e}")

    def remove_directory(self, name):
        """Удаление пустой директории."""
        dir_path = os.path.join(self.current_dir, name)
        if not is_within_working_dir(self.working_dir, dir_path):
            print("Ошибка: Выход за пределы рабочей директории.")
            return
        try:
            os.rmdir(dir_path)
            print(f"Директория '{name}' удалена.")
        except Exception as e:
            print(f"Ошибка: {e}")

    def create_file(self, name):
        """Создание нового файла."""
        file_path = os.path.join(self.current_dir, name)
        if not is_within_working_dir(self.working_dir, file_path):
            print("Ошибка: Выход за пределы рабочей директории.")
            return
        try:
            open(file_path, 'a').close()
            print(f"Файл '{name}' создан.")
        except Exception as e:
            print(f"Ошибка: {e}")

    def delete_file(self, name):
        """Удаление файла."""
        file_path = os.path.join(self.current_dir, name)
        if not is_within_working_dir(self.working_dir, file_path):
            print("Ошибка: Выход за пределы рабочей директории.")
            return
        try:
            os.remove(file_path)
            print(f"Файл '{name}' удален.")
        except Exception as e:
            print(f"Ошибка: {e}")

    def read_file(self, name):
        """Чтение содержимого файла."""
        file_path = os.path.join(self.current_dir, name)
        if not is_within_working_dir(self.working_dir, file_path):
            print("Ошибка: Выход за пределы рабочей директории.")
            return
        try:
            with open(file_path, 'r') as f:
                print(f.read())
        except Exception as e:
            print(f"Ошибка: {e}")

    def write_file(self, name):
        """Запись данных в файл."""
        file_path = os.path.join(self.current_dir, name)
        if not is_within_working_dir(self.working_dir, file_path):
            print("Ошибка: Выход за пределы рабочей директории.")
            return
        try:
            data = input("Введите данные для записи: ")
            with open(file_path, 'w') as f:
                f.write(data)
            print(f"Данные записаны в файл '{name}'.")
        except Exception as e:
            print(f"Ошибка: {e}")

    def copy_item(self, src, dst):
        """Копирование файла или директории."""
        src_path = os.path.join(self.current_dir, src)
        dst_path = os.path.join(self.current_dir, dst)
        if not is_within_working_dir(self.working_dir, src_path) or not is_within_working_dir(self.working_dir, dst_path):
            print("Ошибка: Выход за пределы рабочей директории.")
            return
        try:
            if os.path.isdir(src_path):
                shutil.copytree(src_path, dst_path)
            else:
                shutil.copy2(src_path, dst_path)
            print(f"'{src}' скопирован в '{dst}'.")
        except Exception as e:
            print(f"Ошибка: {e}")

    def move_item(self, src, dst):
        """Перемещение файла или директории."""
        src_path = os.path.join(self.current_dir, src)
        dst_path = os.path.join(self.current_dir, dst)
        if not is_within_working_dir(self.working_dir, src_path) or not is_within_working_dir(self.working_dir, dst_path):
            print("Ошибка: Выход за пределы рабочей директории.")
            return
        try:
            shutil.move(src_path, dst_path)
            print(f"'{src}' перемещен в '{dst}'.")
        except Exception as e:
            print(f"Ошибка: {e}")

    def rename_item(self, old, new):
        """Переименование файла или директории."""
        old_path = os.path.join(self.current_dir, old)
        new_path = os.path.join(self.current_dir, new)
        if not is_within_working_dir(self.working_dir, old_path) or not is_within_working_dir(self.working_dir, new_path):
            print("Ошибка: Выход за пределы рабочей директории.")
            return
        try:
            os.rename(old_path, new_path)
            print(f"'{old}' переименован в '{new}'.")
        except Exception as e:
            print(f"Ошибка: {e}")
