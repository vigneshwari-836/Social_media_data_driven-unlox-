from sklearn.linear_model import LinearRegression
import numpy as np
def predict_trend(df):
    
    # Convert dates to simple numbers (1, 2, 3...)
    X = np.array(range(len(df))).reshape(-1, 1)
    y = df['viral_score'].values
    model = LinearRegression()
    model.fit(X, y)
    # Predict the score for the next 7 days
    future_days = np.array(range(len(df), len(df)+7)).reshape(-1, 1)
    predictions = model.predict(future_days)
    return predictions
