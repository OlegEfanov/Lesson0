import  os
import time

directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(directory, file)        # формирования полного пути к файлам
        filetime = os.path.getmtime(file)               # отображения времени последнего изменения
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime)) # читаемый формат времени
        filesize = os.path.getsize(file)                # получения размера файла.
        parent_dir = os.path.dirname(__file__)          # получения родительской директории файла.
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
          f'Родительская директория: {parent_dir}')

