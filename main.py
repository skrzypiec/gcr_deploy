import os
from model import bmi
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calc")
def calc():
    response = dict()
    response['weigth'] = request.args.get('weigth', type = int)
    response['height_cm'] = request.args.get('height', type = int)

    if response['weigth'] is None or response['height_cm'] is None:
        return jsonify({'error': 'Bad parameters'}), 400

    try:
        response['bmi'] = round(bmi(response['weigth'], response['height_cm']), 2)
    except Exception as e :
        return jsonify({"error" : str(e)})

    response_json = jsonify(response)

    return response_json



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))