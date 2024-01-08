from flask import Flask, request


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def base():
    return "base"

@app.route('/api')
def api_view():
    args = request.args

    return {"result": int(args['result'])}

@app.route('/api/sum')
def sum_view():
    params = request.args

    a = int(params['a'])
    b = int(params['b'])

    return {'result': a + b}



if __name__ == '__main__':
    app.run(debug=True, port=8000)
