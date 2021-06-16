from flask import render_template,Blueprint

games = Blueprint('games',__name__)

@games.route("/gams",methods=['GET','POST'])
def game():
    return render_template("games.html")
