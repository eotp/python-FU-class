def fit_model(model, xs, y):
    return model.fit(xs,y)

def predict(model, xs):
    return model.predict(xs)

def eval_prediction(y_orig, y_predicted):
    return sklearn.metrics.accuracy_score(y_orig, y_predicted)