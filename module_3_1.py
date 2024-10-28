calls = 0

def count_calls():
  global calls
  calls += 1

def string_info(string):
  count_calls()
  print(len(string), string.upper(), string.lower())

def is_containts(string, list_to_searsh):
  count_calls()
  print(string.lower() in [s.lower() for s in list_to_searsh])

    
string_info('Capybara')
string_info('Armageddon')
#string_info(str(input("Введите слово:")))
is_containts('Urban',['ban', 'BaNaN', 'urBAN'])
is_containts('cycle', ['recycling', 'cyclic'])

print(calls)