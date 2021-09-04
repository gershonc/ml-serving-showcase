# Dependencies
from flask import Flask, request, jsonify
import joblib
import traceback
import pandas as pd
import numpy as np
import lightgbm


# Your API definition
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if clf:
        try:
            input_json = request.json
            print(input_json)
            #query = pd.get_dummies(pd.DataFrame(input_json))
            query = pd.DataFrame(input_json)
            print (query) 
            query = query.reindex(columns=feature_names, fill_value=0)
            
            #deal with categorical features
            # Categorical features

            categorical_features(query)
            
            prediction = list(clf.predict(query))
            print (prediction)
            return jsonify({'prediction': str(prediction)})

        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

    
def categorical_features(df):
    categorical_features=[]
    for c in df.columns:
        col_type = df[c].dtype
        if col_type == 'object' or col_type.name == 'category':
            df[c] = df[c].astype(str).astype('category')
            categorical_features.append(c)
    print ('Categorical features: ', categorical_features)
            
            
if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 5000 

    clf = joblib.load("model/model.pkl") # Load "model.pkl"
    print ('Model loaded')
    feature_names = clf.feature_name() # Load "model_columns.pkl"
    print ('features loaded')

    
    app.run(port=port, debug=True)