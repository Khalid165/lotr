from flask import Flask,redirect,render_template,url_for,request
import requests
from flask_bootstrap import Bootstrap


endpoint="https://the-one-api.dev/v2/"
headers = {"Authorization": "Bearer RNV2VpwQrlKV0DwNURjK"}

books = requests.get(f"{endpoint}book")
all_books = books.json()["docs"]



app=Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/books")
def books():

    return render_template("books.html",books=all_books)

@app.route("/chapters")
def chap():

    id=request.args.get("id")
    chapters=requests.get(f"{endpoint}book/{id}/chapter")
    all_chapters=chapters.json()["docs"]
    for book in all_books:
        if book["_id"]==id:
            book_name=book["name"]
    return render_template("chapters.html",chapters=all_chapters,book=book_name)

@app.route("/movies")
def movies():
    respons = requests.get(f"{endpoint}movie", headers=headers)
    all_movies = respons.json()['docs']
    return render_template("movies.html",all_movies=all_movies)

@app.route("/characters",methods=["POST","GET"])
def chars():
    response = requests.get(f"{endpoint}character", headers=headers)
    all_chars = response.json()['docs']
    return render_template("chars.html",chars=all_chars)


if __name__=="__main__":
    app.run(debug=True)

