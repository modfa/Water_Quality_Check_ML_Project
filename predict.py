#import the package
import pickle
from flask import Flask
from flask import request
from flask import jsonify

# Load the model
input_file = './model/model.bin'

#loading the model
with open(input_file, 'rb') as f_in: 
    dv, model = pickle.load(f_in)

app = Flask('watertest')

@app.route('/predict', methods=['POST'])
def predict():
    water_sample = request.get_json()
    #transform the sample to the DV object
    X = dv.transform([water_sample])
    #predict the outcome from the model
    y_pred = model.predict_proba(X)[0, 1]

    sample_potable = y_pred > 0.5
    result = {
        'potability_probability': float(y_pred),
        'Potable': bool(sample_potable)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)