from random import choice
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":
        data = request.form.get("additems").split("\n")
        newdata = dict()
        newdata["kazanan"] = choice(data)
        data.remove(newdata["kazanan"])
        newdata["yedek"] = choice(data)
        return render_template("index.html",willadd=False,data=newdata)
    else:
        return render_template("index.html",willadd=True)

if __name__=="__main__":
    app.run(debug=True,host="192.168.1.32",port=80)