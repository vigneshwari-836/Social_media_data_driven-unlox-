import streamlit as st
import data_engine
import virality_engine
import sentiment_analyzer
import forecaster
import database_handler as db
st.title("UNLOX: Social Engagement AI")
# 1. Get Data
df = data_engine.generate_mock_data()
# 2. Run Virality Engine
df = virality_engine.calculate_virality(df)
# 3. Run NLP Sentiment
df['sentiment_label'] = df['comments'].apply(sentiment_analyzer.get_sentiment)
# 4. Save to Database
db.initialize_database()
db.save_to_db(df)
# 5. Show Visuals
st.subheader("Topic Performance (Virality)")
st.bar_chart(df.set_index('topic')['viral_score'])
st.subheader("Future Forecast")
future_preds = forecaster.predict_trend(df)
st.line_chart(future_preds)
st.write("### Structured Dataset (SQL Output)")
st.dataframe(df)
