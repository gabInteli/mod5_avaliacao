from sqlalchemy import Column, Integer, String, Float 
from models.base import Base 

class Game(Base):
    __tablename__="games"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    platform = Column(String)
    price = Column(Float)
    number = Column(String)

    def __repr__(self):
        return f'Nome do Jogo = {self.name}, Plataforma = {self.platform}, Preço = {self.price}, Quantidade = {self.number}'