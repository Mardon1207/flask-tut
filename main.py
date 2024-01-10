from flask import Flask, request
import json


app = Flask(__name__)


@app.route('/api/sum', methods=["GET", "POST"])
def sum_view():

    if request.method == 'POST':
        form = request.form

        return {"result": int(form['a']) + int(form['b'])}

    else:
        print(request.url)
        return {"error": "method not allowed."}, 404



if __name__ == '__main__':
    app.run(debug=True)
