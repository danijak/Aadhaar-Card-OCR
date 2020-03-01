from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'javed ali',
        'title': 'rahul master',
        'content': 'Second post content',
        'date_posted': 'Feb 2, 2020'
    }
]


@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title='DocOcr')


@app.route("/about")
def about():
    return render_template('about.html', title='javed')


if __name__ == '__main__':
    app.run(debug=True)
