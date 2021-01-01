from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    Price = int(request.form['Price'])
    Rooms = int(request.form['Rooms'])

    response = jsonify({
        'estimated_ROI': util.predict_roi(Price. Rooms)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
if __name__ == '__main__':
    print('starting server...')
    app.run()