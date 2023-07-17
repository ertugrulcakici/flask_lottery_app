from random import choice

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form.get("additems").split("\n")
        newdata = dict()
        newdata["winner"] = choice(data)
        data.remove(newdata["winner"])
        newdata["Subsitute"] = choice(data)
        return render_template("index.html", willadd=False, data=newdata)
    else:
        return render_template("index.html", willadd=True)


if __name__ == "__main__":
    app.run(host="localhost", port=8080)
