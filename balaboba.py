import requests

# Переменные query и genre - это параметры для POST-запроса к балабобе https://yandex.ru/lab/yalm.
# Придумайте ключевую фразу для запроса к Балабобе
# и передайте ее в переменную query
query = "Овен"
# Присвойте числовое значение (id жанра) переменной genre. Это выберет один и
genre = 10


def get_genres():
    """
    Функция отправляет запрос к Балабобе,
    и получает в ответ список жанров.
    """
    genres_url = 'https://zeapi.yandex.net/lab/api/yalm/intros'
    try:
        response = requests.get(genres_url)
        response = response.json()
        genres_list = response["intros"]
    except:
        print('Во время выполнения функции get_genres() возникла ошибка!')
        genres_list = []
    return genres_list


def print_genres(genres_list):
    """
    Печатает в форматированном виде список доступных жанров,
    полученный из функции get_genres()
    genres: ответ от функции get_genres(), который нужно распечатать
    """
    print("Список жанров, в которых можно продолжить фразу:")
    for genre_info in genres_list:
        genre_out = ""
        for genre_element in genre_info:
            genre_out = f'{genre_out} {genre_element} -'
        l = len(genre_out)
        Remove_last = genre_out[:-1]
        print (Remove_last)


def generate_text(query, genre):
    """
    Функция отправляет POST-запрос к Балабобе,
    и получает ответ в виде словаря.
    Параметры POST-запроса:
    query: ключевая фраза
    genre: id жанра, в котором Балабоба должен сгенерировать текст
    """
    text_url = 'https://zeapi.yandex.net/lab/api/yalm/text3'
    data = {
        "query": query,
        "intro": genre
    }
    try:
        response = requests.post(url=text_url, json=data)
        dict_response = response.json()
    except:
        print('Во время выполнения функции get_genres() возникла ошибка!')
        dict_response = {}
    return dict_response


def print_text(text_dict):
    """
    Печатает текст ответа в форматированном виде.
    dict_response: ответ на запрос в виде словаря
    """
    print('\n' + 'Ответ на ваш запрос:' + '\n')
    print (f'{text_dict["query"]} {text_dict["text"]}')



genres_list = get_genres()
print_genres(genres_list)
text_dict = generate_text(query, genre)
print_text(text_dict)