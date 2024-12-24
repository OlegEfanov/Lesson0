class WordsFinder:
    def __init__ (self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        words = []
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for p in punctuation:
                        line = line.replace(p, ' ')
                    line = line.replace(' - ', ' ')
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        list_ = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                list_[name] = words.index(word.lower()) + 1
        return list_

    def count(self, word):
        counters = {}
        for name, words in self.get_all_words().items():
            words_count = words.count(word.lower())
            counters[name] = words_count

        return counters

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}

