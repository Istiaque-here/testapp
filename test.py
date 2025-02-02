from flask import Flask, render_template

app = Flask(__name__)

blogs = [
    {
        'author':'mark',
        'title':'hello world',
        'content':'hi this mark from nowhere',
        'date_posted':'january 31,2025'
    },
    {
        'author':'twain',
        'title':'hello mars',
        'content':'hi this twain from mars',
        'date_posted':'february 1,2025'
    },
]
@app.route('/')
def home():
    # return "Hello, Flask in Codespaces! Myself Istiaque here."
    return render_template('home.html',posts=blogs)

@app.route('/about')
def about():
    return render_template('about.html',title='Istiaque')

app.run(debug=True)