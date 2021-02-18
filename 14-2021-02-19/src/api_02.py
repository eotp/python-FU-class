from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

X = iris['data']
y = iris['target']
# Split dataset into training and test data
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# n_jobs = -1 allows to use all our available computing power
global rf
rf = RandomForestClassifier(n_jobs=-1, random_state=1)

def fit_model(model, xs, y):
    return model.fit(xs,y)

def predict(model, xs):
    return model.predict(xs)

def eval_prediction(y_orig, y_predicted):
    return accuracy_score(y_orig, y_predicted)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/model/reset")
def model_reset():
    global rf 
    rf = RandomForestClassifier(n_jobs=-1, random_state=1)
    return {"message": "Model reset"}

@app.get("/model/train")
def model_train():
    global rf 
    try:
        rf = fit_model(rf,x_train,y_train)
        return {"message": "Model trained"}
    except Exception as e:
        return {"Error": e}

@app.get("/model/info")
def model_info():
    return {"model_info": "RandomForestRegressor"}

@app.get("/model/eval")
def model_eval():
    return {"Accuracy Score": eval_prediction(y_test, predict(rf, x_test))}
    
@app.get("/model/predict/{sepal_length},{sepal_width},{petal_length},{petal_width}")    
def model_predict(sepal_length, sepal_width, petal_length, petal_width):
    to_predict = np.array([sepal_length, sepal_width, petal_length, petal_width]).reshape(1,-1)
    prediction = rf.predict(to_predict)[0]
    predicted_class = iris['target_names'][prediction]
    return {"Input": {
                        "Sepal Length": sepal_length,
                        "Sepal Width": sepal_width,
                        "Petal Length": petal_length,
                        "Petal Width": petal_width
                    },
            "Predicted class name": predicted_class,
            "Predicted class": f"{prediction}"
           }
