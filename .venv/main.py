from flask import Flask

app = Flask(__name__)

@app.route("/")
def ola_mundo():
    return "<h1><p>Olá, Mundo!</p></h1>"

if __name__ == '__main__':
    app.run(port=5000, debug=True)