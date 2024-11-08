def singl_root_words (root_word, *other_words):
    same_words = []                                     #Создаем внутри функции пустой список.
    for i in other_words:                               #Присваиваем i первое значение из последовательности other_words
        if root_word.lower() in i.lower() or i.lower() in root_word.lower(): #Если root_word есть в i или наоборот то
            same_words.append(i)                        #Добавляем значение в список same_words
    return same_words                                   #Возвращаем список после перебора *other_worlds.

result1 = singl_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = singl_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
