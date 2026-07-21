import pandas as pd
import numpy as np

def generate_mock_data():
    
    data = {
        'date': pd.date_range(start='2024-01-01', periods=30),
        'topic': ['Social Anxiety', 'Dating Tips', 'Career Growth', 'Friendship']*7 + ['Dating Tips', 'Career Growth'],
        'likes': np.random.randint(100, 1000, 30),
        'shares': np.random.randint(10, 300, 30),
        'saves': np.random.randint(20, 400, 30),
        'comments': ["This changed my life", "I don't agree", "So relatable!", "Helpful"]*7 + ["Amazing", "Wow"]
    }
    return pd.DataFrame(data)
