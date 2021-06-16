from flask import render_template, Blueprint, redirect, url_for
from my_project.games.millioner.forms import PLAY_Form
from flask_login import current_user
from my_project import db
import random

mill = Blueprint('mill', __name__)

with open("file1.txt") as f:
    fc = f.read().strip().split("\n")

lis = []
for i in fc:
    lis.append(i.split(":"))
rands = random.randrange(len(lis))
num = lis[rands]
number = 0


@mill.route("/millioner", methods=["GET", "POST"])
def millioner():
    global num
    form = PLAY_Form()
    fnum = form.fnum.data
    info = ""
    return render_template("game.html", form=form, fnum=fnum, mylis=num, info=info)


@mill.route("/millioners", methods=["GET", "POST"])
def millioner_check():
    global num
    global number
    form = PLAY_Form()
    fnum = form.fnum.data
    for i in lis:
        if i == num:
            lis.remove(i)
    if len(lis) != 0:
        if fnum == num[2]:
            info = "Right"
            number += 1
            rands = random.randrange(len(lis))
            num = lis[rands]
            return render_template("game.html", form=form, fnum=fnum, mylis=num, info=info, number=number)
        else:
            rands = random.randrange(len(lis))
            num = lis[rands]
            info = "Wrong"
            return render_template("game.html", form=form, fnum=fnum, mylis=num, info=info, number=number)
    else:
        if fnum == num[2]:
            number += 1
        info = f"Game over!Your score is {number}/10!"
        current_user.numbers = number
        db.session.commit()
        return redirect(url_for('users.check_dashboard'))

