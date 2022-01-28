from sqlalchemy import Column, Integer, String, ForeignKey
from films_db import Base, engine

class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"Film: {self.name}"

class User_Request(Base):
    __tablename__ = 'user_requsts'
    id = Column(Integer, unique=True, primary_key=True)
    film_id = Column(Integer, ForeignKey(Film.id), nullable=False)
    user_film_name = Column(String)

class Urls(Base):
    __tablename__ = 'urls'

    id = Column(Integer, unique=True, primary_key=True)
    film_id = Column(Integer, ForeignKey(Film.id), nullable=False)
    kp_url = Column(String)
    netflix_url = Column(String)
    okko_url = Column(String)
    ivi_url = Column(String)

    def __repr__(self):
        return f'Urls id: {self.id}, KP {self.kp_url}, Netflix {self.netflix_url}, Okko {self.okko_url}, ivi {self.ivi_url}'

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)