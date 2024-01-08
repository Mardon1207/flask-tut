from flask import Flask, request


app = Flask(__name__)


@app.route('/api/sum', methods=["GET", "POST"])
def sum_view():

    if request.method == 'POST':
        params = request.args

        a = int(params['a'])
        b = int(params['b'])

        return {'result': a + b}

    else:
        print(request.url)
        return {"error": "method not allowed."}



if __name__ == '__main__':
    app.run(debug=True, port=8000)
