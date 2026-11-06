from flask import Flask, render_template, abort, request, redirect
from models import Book
app = Flask(__name__)

@app.route("/books")
def book_list():
    books = Book.all()
    return render_template("books.html", books=books)

@app.route("/books/<int:id>")
def book_detail(id):
    book = Book.load(id)
    if book is None:
        abort(404)
    return render_template("book.html", book=book)

@app.route("/books/add", methods=["GET", "POST"])
def book_add():
    if request.method == "POST":
        book = Book(
            request.form["title"],
            request.form["author"],
            int(request.form["year"]),
        )
        book.save()
        return redirect("/books")

    empty = Book("", "", "")
    return render_template(
        "form.html",
        book=empty,
        heading="Add a book",
    )

@app.route("/books/<int:id>/edit", methods=["GET", "POST"])
def book_edit(id):
    book = Book.load(id)

    if book is None:
        abort(404)

    if request.method == "POST":
        book.title = request.form["title"]
        book.author = request.form["author"]
        book.year = int(request.form["year"])
        book.update()
        return redirect(f"/books/{id}")

    return render_template(
        "form.html",
        book=book,
        heading="Edit a book",
    )