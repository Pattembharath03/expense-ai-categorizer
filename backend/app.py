from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)

# Enable CORS
CORS(app)

# Load AI model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json

    text = data['text']

    prediction = model.predict([text])[0]

    return jsonify({
        "category": prediction
    })

if __name__ == '__main__':
    app.run(debug=True)