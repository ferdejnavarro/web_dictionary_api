from flask import Flask, render_template
import pandas as pd
import requests

app = Flask(__name__)

# df = pd.read_csv('dictionary.csv')
API_URL = 'https://api.dictionaryapi.dev/api/v2/entries/en/'

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>/")
# def dictionary(word):
#     definition = df.loc[df['word'] == word]['definition'].squeeze()
#     dictionary = {"definition": definition,
#             "word": word}
#     return dictionary
def api(word):
    response = requests.get(API_URL + word)
    data = response.json()
    definition = data[0]["meanings"][0]["definitions"][0]["definition"]
    dictionary = {"definition": definition,
                 "word": word}
    return dictionary


if __name__ == "__main__":
    app.run(debug=True, port=5001)
