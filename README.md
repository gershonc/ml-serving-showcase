# ML-Serving-Showcase

Implementation of a ML Model Serving with Flask, the model is LGBM trained on Kaggle titanic data.
To run the service:
> python .\ml_serving.py

To test the service go to the following URL: http://127.0.0.1:5000/predict

Here is an input for example (JSON format):
```json
[
    {"Age": 85, "Sex": "male", "Embarked": "S", "Pclass": 3},
    {"Age": 63, "Sex": "female", "Embarked": "C", "Pclass": 2},
    {"Age": 15, "Sex": "male", "Embarked": "Q", "Pclass": 1}
]
```

Here is an example of the API on POSTMAN:
![alt text](https://github.com/gershonc/ml-serving-showcase/blob/main/img/postman_serving_ml.png?raw=true)

