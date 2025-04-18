# File Manager

Базовый файловый менеджер с текстовым интерфейсом, разработанный на Python. Он позволяет выполнять основные операции с файлами и директориями внутри заданной рабочей директории.

---

## **Описание проекта**

Файловый менеджер предоставляет пользователю возможность управлять файлами и директориями через командную строку. Программа изолирует пользователя в пределах рабочей директории, предотвращая выход за её границы. Она поддерживает создание, удаление, копирование, перемещение и переименование файлов и директорий, а также чтение и запись данных в файлы.

---

## **Функционал**

### Основные функции:

1. **Навигация по файловой системе**:
   - Переход между директориями.
   - Просмотр содержимого текущей директории.

2. **Работа с директориями**:
   - Создание новой директории.
   - Удаление пустой директории.

3. **Работа с файлами**:
   - Создание нового файла.
   - Удаление файла.
   - Чтение содержимого файла.
   - Запись данных в файл.

4. **Дополнительные операции**:
   - Копирование файлов и директорий.
   - Перемещение файлов и директорий.
   - Переименование файлов и директорий.

---

## **Принципы организации кода**

1. **Модульность**:
   - Код разделён на несколько модулей для удобства поддержки и расширения:
     - `config.py`: Настройки программы (например, путь к рабочей директории).
     - `utils.py`: Вспомогательные функции (например, проверка выхода за пределы рабочей директории).
     - `file_manager.py`: Логика файлового менеджера (класс `FileManager`).
     - `main.py`: Точка входа в программу.

2. **Изоляция рабочей директории**:
   - Программа предотвращает выход пользователя за пределы рабочей директории с помощью функции `is_within_working_dir`.

3. **Кроссплатформенность**:
   - Используются стандартные библиотеки Python (`os`, `shutil`), что обеспечивает совместимость с Windows и UNIX-подобными системами.

4. **Читаемость кода**:
   - Каждая функция имеет чёткое назначение и документацию.
   - Команды обрабатываются в цикле, что делает код легко расширяемым.

---

## **Установка и запуск**

### **Требования**
- Python 3.6 или выше.

### **Шаги установки**
1. Склонируйте репозиторий или создайте файлы проекта вручную:
   ```bash
   git clone https://github.com/GrishaevArtyom/lab_file_manager.git
   cd file-manager
   ```

2. Убедитесь, что все файлы проекта находятся в одной директории:
   - `config.py`
   - `utils.py`
   - `file_manager.py`
   - `main.py`

3. Откройте файл `config.py` и укажите путь к рабочей директории:
   ```python
   WORKING_DIR = "/path/to/your/working/directory"
   ```

4. Запустите программу:
   ```bash
   python main.py
   ```

---

## **Команды**

### **Навигация**
- `cd <path>`: Перейти в указанную директорию.
- `ls`: Показать содержимое текущей директории.

### **Работа с директориями**
- `mkdir <name>`: Создать новую директорию.
- `rmdir <name>`: Удалить пустую директорию.

### **Работа с файлами**
- `touch <name>`: Создать новый файл.
- `rm <name>`: Удалить файл.
- `read <name>`: Прочитать содержимое файла.
- `write <name>`: Записать данные в файл.

### **Дополнительные операции**
- `copy <src> <dst>`: Скопировать файл или директорию.
- `move <src> <dst>`: Переместить файл или директорию.
- `rename <old> <new>`: Переименовать файл или директорию.

### **Выход**
- `help`: Показать эту справку.
- `exit`: Завершить работу программы.

---

## **Пример использования**

```bash
/path/to/working/directory> ls
file1.txt
folder1

/path/to/working/directory> mkdir new_folder
Директория 'new_folder' создана.

/path/to/working/directory> cd new_folder
/path/to/working/directory/new_folder> touch new_file.txt
Файл 'new_file.txt' создан.

/path/to/working/directory/new_folder> write new_file.txt
Введите данные для записи: Hello, World!
Данные записаны в файл 'new_file.txt'.

/path/to/working/directory/new_folder> read new_file.txt
Hello, World!

/path/to/working/directory/new_folder> exit
Выход из программы.
```