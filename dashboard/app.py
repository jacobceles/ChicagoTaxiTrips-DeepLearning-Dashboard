import keras
import calendar
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
models = {
    "2015": keras.models.load_model("NN_model"),
    "2016": keras.models.load_model("NN_model"),
    "2017": keras.models.load_model("NN_model"),
    "2018": keras.models.load_model("NN_model"),
    "2019": keras.models.load_model("NN_model"),
    "2020": keras.models.load_model("NN_model"),
    "2021": keras.models.load_model("NN_model")
}


@app.route('/prediction', methods=['POST', 'GET'])
def get_prediction():
    month = request.args.get('month', default=2, type=int)
    seconds = request.args.get('seconds', default=50.0, type=float)
    distance = request.args.get('distance', default=50.0, type=float)
    fares = []
    years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021"]
    for model in models.values():
        fares.append(str(model.predict([[seconds, distance, month]])[0][0]))
    """
    result = "In the month of {0}, if you rode a taxi in Chicago for {1} minutes to cover a distance of {2} miles, it" \
             " would have cost you ${3}!".format(calendar.month_name[month], seconds/60, distance, str(round(fare, 2)))
    """
    return jsonify(labels=years, values=fares)


@app.route("/")
def get_home_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='localhost', port=5001)
