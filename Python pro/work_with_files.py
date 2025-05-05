from pathlib import Path

# # Получить текущую папку
# p = Path.cwd()
# print(p)

# # Создать новый путь
# new_dir = p / "example_folder"
# print(new_dir)

# # Создание папки (если не существует)
# new_dir.mkdir(exist_ok=True)

# # Создание файла
# file_path = new_dir / "file.txt"
# file_path.write_text("Пример текста")

# # Чтение файла
# content = file_path.read_text()
# print("Содержимое:", content)

# # Удаление файла
# file_path.unlink()
####
p = Path.cwd()
new_dir = p / "data"
new_dir.mkdir(exist_ok=True)
file_path = new_dir / "log.txt"
file_path.write_text("logs")
print("Содержимое:", file_path.read_text())