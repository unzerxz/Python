from flask import Flask

app = Flask(__name__)

@app.route("/")
def ola_mundo():
    return "<p>Olá, Mundo!</p>"

if __name__ == '__main__':
    app.run(port=5000, debug=True)