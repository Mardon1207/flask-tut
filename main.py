from flask import Flask, request
import json


app = Flask(__name__)


@app.route('/api/sum/<int:a>/<int:b>', methods=["GET", "POST"])
def sum_view(a: int, b: int):

    if request.method == 'POST':

        return {"result": a + b}

    else:
        print(request.url)
        return {"error": "method not allowed."}, 404



if __name__ == '__main__':
    app.run(debug=True)
