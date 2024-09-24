import streamlit as st
import joblib
import sklearn

model=joblib.load("model.bkl")

def Prediction(mail):
    res = model.predict([mail])
    return res[0]

def Main():
    st.title("MAIL IMPORTANCE DETECTOR")
    mail = st.text_input("enter the mail in order to check it's importance")
    if st.button("predict"):
        res = Prediction(mail)
        list_text = ["this mail is spam and might have something suspecious" , "this mail is ham and important"]
        st.text(f"{list_text[res]}")
st.text("model accuracy score is 98%-Bernoulli Naive_Baye ")
Main()

