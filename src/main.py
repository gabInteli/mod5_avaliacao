from flask import Flask, render_template, redirect, request
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base
from models.game import Game

app = Flask(__name__)

engine = create_engine("sqlite:///register.db", echo = True)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

@app.route("/")
def index():
    register1 = Game(name = "DEAD SPACE REMAKE", platform = "PS5", price= 350.00, number= 10)
    register2 = Game(name = "FORSPOKEN ", platform = "PC", price=299.00, number=8)
    register3 = Game(name = "DEAD ISLAND 2", platform = "PS5", price=350.00, number=10)
    register4 = Game(name = "HOGWARTS LEGACY", platform = "PC", price=219.00, number=7)
    register5 = Game(name = "WILD HEARTS", platform = "XBOX Series", price=350.00, number=7)
    register6 = Game(name = "RESIDENT EVIL 4", platform = "PS5", price=289.00, number=10)
    register7 = Game(name = "THE LEGEND OF ZELDA: TEARS OF THE KINGDOM", platform = "Switch", price=350.00, number=10)

    games_list = [register1, register2, register3, register4, register5, register6, register7]

    for i in range(0,6):
        session.add(games_list[i])
    
    session.commit()
    games_list = session.query(Game).all()
    print(games_list)
    
    return render_template("index.html", Games = games_list)