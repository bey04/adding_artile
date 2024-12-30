from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="blog_db"
)
cursor = db.cursor()

# Homepage - List of articles
@app.route("/")
def index():
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    return render_template("index.html", posts=posts)

# Add a new article
@app.route("/add", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", (title, content))
        db.commit()
        return redirect("/")
    return render_template("add_post.html")

if __name__ == "__main__":
    app.run(debug=True)
