from flask import Flask, request, jsonify
import testingutil

app = Flask(__name__)

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    Price = int(request.form['Price'])
    Rooms = int(request.form['Rooms'])

    response = jsonify({
        'estimated_price': testingutil.get_estimated_price(Price, Rooms)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run()