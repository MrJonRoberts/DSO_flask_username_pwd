from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # do something
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        if username == "bob" and password == "1234":
            return render_template("admin.html", name=username)
        else:
            return render_template("home.html", error="Wrong username and password")
    else:

        return render_template("home.html")


if __name__ == '__main__':
    app.run()
