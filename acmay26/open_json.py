import json #библиотека хранение передача информации от сервера к клиенту

# d = {'black':'черный', #словарь
#      'white':'белый'}
# with open ('dict.json', 'w', encoding =  'utf-8') as f: # словарь положили в файл
#     json.dump(d, f, indent=4) # 4 -это отступ, dump способ записи

with open('dict.json', 'r', encoding='utf-8') as f:
    d = json.load(f)# способ чтения 
while True:
    word = input('Введите слово для перевода:')
    if word in d:
        print(f' {word} - {d[word]}')
    elif word == 'q':
        break
    else:
        transl = input(f'Введите перевод слова - {word}: ')
        d[word] = transl
        with open ('dict.json', 'w', encoding =  'utf-8') as f: #переписался весь словарь
            json.dump(d,f, indent=4)
