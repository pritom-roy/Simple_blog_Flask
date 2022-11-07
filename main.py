import os

import requests
from flask import Flask, render_template

app = Flask(__name__)

JASON_BIN = os.environ['link']
response = requests.get(url=JASON_BIN)
post = response.json()

@app.route('/')
def home():

    return render_template("index.html", num=post)

@app.route('/post/<int:idvalue>')
def readPost(idvalue):
    return render_template("post.html", val=idvalue, num=post)



if __name__ == "__main__":
    app.run(debug=True)
