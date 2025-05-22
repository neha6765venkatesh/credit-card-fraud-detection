import streamlit as st
from utils import preprocess_input, predict

st.set_page_config(page_title="Credit Card Fraud Detector")
st.title("💳 Credit Card Fraud Detection App")

st.markdown("Please fill in the transaction details below:")

category = st.selectbox("Merchant Category", ['gas_transport', 'grocery_net', 'grocery_pos', 'shopping_pos'])
amt = st.number_input("Transaction Amount ($)", min_value=0.0, step=0.01)
gender = st.selectbox("Cardholder Gender", ['Male', 'Female'])
city_pop = st.number_input("City Population", min_value=0)

if st.button("Predict Fraud"):
    data = preprocess_input(category, amt, gender, city_pop)
    result = predict(data)
    if result == 1:
        st.error("🚨 Alert: This transaction is likely **fraudulent**!")
    else:
        st.success("✅ This transaction appears to be **legitimate**.")