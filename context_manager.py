import datetime
import time

class File(object):
    def __init__(self, file_name, method):
        self.file_object = open(file_name, method)

    def __enter__(self):
        print(f'Запуск программы в: {datetime.datetime.utcnow()}')
        self.time = time.time()
        return self.file_object

    def __exit__(self, type, value, traceback):
        print(f'Выход из программы в: {datetime.datetime.utcnow()}')
        print(f"время работы программы: {time.time() - self.time}")
        self.file_object.close()

lines = ''
with open('cookbook.txt', encoding='utf-8') as file:
    for line in file:
        lines = line.strip()
        start_time = time.time()

with File('cookbook.txt', 'w') as opened_file:
    opened_file.write(lines)
   



