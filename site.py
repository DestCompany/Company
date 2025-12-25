from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_rates():
    url = "https://api.exchangerate.host/latest?base=USD"
    data = requests.get(url).json()
    return {
        "EUR": data["rates"]["EUR"],
        "RUB": data["rates"]["RUB"],
        "KZT": data["rates"]["KZT"]
    }

@app.route("/")
def index():
    rates = get_rates()
    return render_template("index.html", rates=rates)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
