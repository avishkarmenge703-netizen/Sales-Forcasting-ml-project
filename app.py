import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("../model/sales_model.pkl")

st.title("Sales Forecasting ML App")

st.write("Enter product details to predict future sales.")

store_id = st.number_input("Store ID", min_value=1)
product_id = st.number_input("Product ID", min_value=1)
price = st.number_input("Price", min_value=0.0)
promotion = st.selectbox("Promotion", [0,1])
holiday = st.selectbox("Holiday", [0,1])

input_data = pd.DataFrame({
    "store_id":[store_id],
    "product_id":[product_id],
    "price":[price],
    "promotion":[promotion],
    "holiday":[holiday]
})

if st.button("Predict Sales"):
    
    prediction = model.predict(input_data)
    
    st.success(f"Predicted Sales: {prediction[0]:.2f}")
