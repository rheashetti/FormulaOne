import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

df = get_historical_data([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022], 7)

encoder = LabelEncoder()
df["driver"] = encoder.fit_transform(df["driver"])

features = ["driver", "circuit", "year"]
target = "position"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)