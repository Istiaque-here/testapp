from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask in Codespaces! Myself Istiaque here."

app.run(debug=True)
