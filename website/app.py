#import numpy as np
import pandas as pd
from sklearn import preprocessing
from flask import Flask, request, render_template
from keras.models import load_model
from joblib import load
from pathlib import Path

app = Flask(__name__)

THIS_FOLDER = Path(__file__).parent.resolve()
model = load_model(str(THIS_FOLDER / "models/model.h5"))

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    inputs = [float(x) for x in request.form.values()]
    
    inputs.insert(2, inputs[0]/((inputs[1]/100)*(inputs[1]/100)))
    inputs.insert(10, max(inputs[4], inputs[6], inputs[8]) + max(inputs[5], inputs[7], inputs[9]))
   
    features = ['BMXWT', 'BMXHT', 'BMXBMI', 'RIDAGEYR', 'MGXH1T1', 'MGXH2T1', 'MGXH1T2', 'MGXH2T2', 'MGXH1T3', 'MGXH2T3', 'MGDCGSZ', 'RIAGENDR']
    x = pd.DataFrame([inputs], columns=features);

    numiric_cols = ['BMXWT', 'BMXHT', 'BMXBMI', 'RIDAGEYR', 'MGXH1T1', 'MGXH2T1', 'MGXH1T2', 'MGXH2T2', 'MGXH1T3', 'MGXH2T3', 'MGDCGSZ']
    scaler = preprocessing.StandardScaler().fit(x[numiric_cols])
    x_scaled = scaler.transform(x[numiric_cols])
    x_scaled = pd.DataFrame(x_scaled, index=x.index, columns=x[numiric_cols].columns)
    x_scaled = pd.concat([x_scaled, x['RIAGENDR']], axis=1)
    x_scaled

    prediction = model.predict(x)
    output = prediction[0][0]

    return render_template('index.html', prediction_text='Percent with osteoporosis is {}'.format(output))

if __name__ == '__main__':
   app.run(debug = True)
