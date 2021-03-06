from application import app
from collections import User
from flask import redirect, url_for, abort, session, render_template
from hashlib import sha224
from os import urandom

@app.route("/judge")
def judge():
    if not session.get("logged_in"):
        abort(404)

    user = User.objects.get(alias = session.get("alias"))

    if not user.isJudge:
        abort(404)

    return render_template("judge_portal/index.html", user = user)

@app.route("/generate-judge-key")
def generateJudgeKey():
    if not session.get("logged_in"):
        abort(404)

    user = User.objects.get(alias = session.get("alias"))

    if not user.isJudge:
        abort(404)
    key = urandom(1000).encode("base_64").replace("=","")
    user.judgeKey = sha224(key).hexdigest()
    user.save()
    return render_template("judge_portal/judgekey.html", key = key)
