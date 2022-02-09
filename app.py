from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    name = "Mr Roberts"
    return render_template("home.html", name=name)


if __name__ == '__main__':
    app.run()
