from flask import Flask


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def base():
    return "base"

@app.route('/about')
def about_view():
    return "about"



if __name__ == '__main__':
    app.run(debug=True, port=8000)
