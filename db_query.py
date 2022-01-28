from films_db import db_session
from film_model import Film, Urls, User_Request

# Поиск по базе

def get_film_id(film_name):
    film_id = db_session.query(Film.id).filter(Film.name==film_name).first()
    return film_id

def find_film_urls(film_name):
    urls_list = db_session.query(Urls.kp_url, Urls.netflix_url, Urls.okko_url, Urls.ivi_url).filter(Urls.film_id==get_film_id(film_name)[0]).first()
    return urls_list

# Добавление в базу Названия
def save_film(film_name):
    film = Film(name=film_name)
    db_session.add(film)
    db_session.commit()

# Добавление в базу ссылок
def save_urls(film_name, url1, url2, url3, url4):
    id = get_film_id(film_name)[0]
    urls_add = Urls(film_id=id, kp_url=url1, netflix_url=url2, okko_url=url3, ivi_url=url4)
    db_session.add(urls_add)
    db_session.commit()

# Добавление в базу запроса пользователя 
def save_user_request(film_real_name, user_film_request):
    id = get_film_id(film_real_name)[0]
    user_request_add = User_Request(film_id=id, user_film_name=user_film_request)
    db_session.add(user_request_add)
    db_session.commit()
