def calculate_virality(df):
   
    # We create a new column called 'viral_score'
    df['viral_score'] = (df['shares'] + df['saves']) / df['likes']
    return df