from pprint import pprint

def custom_write(file_name, strings):
    dict_ = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(len(strings)):
        t = file.tell()
        file.write(str(strings[i] + "\n"))
        dict_[(i + 1, t)] = strings[i]

    file.close()
    return dict_

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)