from flask import Flask, request
import json


app = Flask(__name__)


@app.route('/api/sum', methods=["GET", "POST"])
def sum_view():

    if request.method == 'POST':
        json_data = request.json
        print(type(json_data))

        return {}

    else:
        print(request.url)
        return {"error": "method not allowed."}, 404



if __name__ == '__main__':
    app.run(debug=True)
