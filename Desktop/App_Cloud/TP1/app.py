from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, i'm Benyamani Chaimaa and i'm an engineering student Data Science et Cloud Computing"

if __name__ == "__main__":
    app.run()
