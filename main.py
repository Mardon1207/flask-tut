from flask import Flask, request, render_template
import json


app = Flask(__name__)


@app.route('/<int:n>')
def home_view(n: int):

    nums = list(range(n))

    return render_template('index.html', context={"nums": nums, "n": n})



if __name__ == '__main__':
    app.run(debug=True)
