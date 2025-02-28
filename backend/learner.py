import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
import f1data

def predict_performance(circuit, driver):
    """Predicts the performance of the driver in the given circuit and year"""
    
    results = f1data.get_historical_data(circuit, driver)
    print(results)
    df = pd.DataFrame(results.items(), columns=['year', 'position'])
    print(df)
    df['position'] = df['position'].astype(int)

    X = df[['year']]
    y = df['position'] 

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    
    return np.sqrt(mse)

print(predict_performance("monza", "hamilton"))