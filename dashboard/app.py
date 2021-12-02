from flask import Flask, request
from flask import render_template

app = Flask(__name__)


@app.route('/updateData', methods=['POST'])
def get_prediction():
    a = request.form['labels0']
    return "success", 201


@app.route("/")
def get_home_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='localhost', port=5001)
