from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from database import get_db, close_db
from forms import GuessForm
from random import randint

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'
Session(app)
app.teardown_appcontext(close_db)
app.config["SECRET_KEY"] = "this-is-my-secret-key"


@app.route("/shop", methods=["GET", "POST"])
def shop():

    return render_template("shop.html")

@app.route("/fish", methods=["GET", "POST"])
def fish():
    
    return render_template("fish.html")


# @app.route("/cart")
# def cart(): 
#     if "cart" not in session: 
#         session["cart"] = {}

#     names = {}
#     db = get_db()
#     for wine_id in session["cart"]:
#         wine = db.execute('''SELECT*
#                              FROM wines
#                              WHERE wine_id =?;''', (wine_id, )).fetchone()
        
#         name = wine["name"]
#         names[wine_id] = name

#     return render_template("cart.html", cart=session["cart"], names=names )

# @app.route("/add_to_cart/<int:wine_id>")
# def add_to_cart(wine_id):
#     if "cart" not in session: 
#         session["cart"] = {}

#     #looking if the wine id is in the cart already, if the item is not in there, adds it to there
#     if wine_id not in session["cart"]:
#         session["cart"][wine_id] = 1
#     #if it's already been bought before, at least 1, buying another one
#     else: 
#         session["cart"][wine_id] = session["cart"][wine_id] + 1
#     return redirect(url_for("cart"))