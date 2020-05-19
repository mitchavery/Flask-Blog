from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Mitch Avery', 
        'title': 'Blog Post 1', 
        'content': 'First post content', 
        'date': 'April 2020'
    }, 
    {
        'author': 'Kyle ', 
        'title': 'Blog Post 2', 
        'content': 'First post2 content', 
        'date': 'April2 2020'
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.htm', posts=posts)


@app.route("/about")
def about():
    return render_template('about.htm')


if __name__ == "__main__":
    app.run(debug=True)