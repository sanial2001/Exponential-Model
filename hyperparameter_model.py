import optuna
train_data, test_data = df[0:20], df[20:]

def objective_smoothing(trial):
    X,y=train_data,train_data
    seasonal=trial.suggest_categorical("seasonal",["add", "mul", "additive", "multiplicative", None])
    trend=trial.suggest_categorical("trend",["add", "mul", "additive", "multiplicative", None])
    initialization_method=trial.suggest_categorical("initialization_method",['estimated','heuristic', 'legacy-heuristic'])
    mdl=ExponentialSmoothing(train_data,trend=trend,seasonal=seasonal,initialization_method=initialization_method)
    mdl = mdl.fit(optimized=True) #disp=0
    predictions = mdl.forecast(len(test_data))
    predictions = pd.Series(predictions)
    residuals = test_data['y'] - predictions
    # print(residuals)
    mse=np.sqrt(np.mean(residuals**2))
    accuracy=mse
    return accuracy

studys=optuna.create_study(direction="minimize")
studys.optimize(objective_smoothing,n_trials=10)
