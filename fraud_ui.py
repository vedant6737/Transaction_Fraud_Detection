import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_detection_pipeline.pkl")

st.title("Fraud Detection System")
st.markdown("Enter Transaction details:")
st.divider()

transaction_type = st.selectbox(
    "Transaction Type:",
    ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'CASH_IN', 'DEBIT']
)

amount = st.number_input("Amount:", min_value=0.0, value=1000.0)

oldbalanceOrg = st.number_input("Sender's Old Balance:", min_value=0.0, value=7000.0)
newbalanceOrig = st.number_input("Sender's New Balance:", min_value=0.0, value=5000.0)

oldbalanceDest = st.number_input("Receiver's Old Balance:", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("Receiver's New Balance:", min_value=0.0, value=0.0)

if st.button("Predict"):
    input_data = pd.DataFrame([{
        'type': transaction_type,
        'amount': amount,
        'oldbalanceOrg': oldbalanceOrg,
        'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDest,
        'newbalanceDest': newbalanceDest
    }])

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: {int(prediction)}")

    if prediction == 1:
        st.error("WARNING! Transaction may be Fraud")
    else:
        st.success("Transaction looks Legit")

#To run web app open Terminal
#cd ~/PycharmProjects/Fraud_detection
#streamlit run fraud_ui.py