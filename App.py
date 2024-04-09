import streamlit as st
import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

pickle_in = open("best_model.unknown","rb")
classifier = pickle.load(pickle_in)


def welcome():
    return "Hello Welcome All"

def feedback(Age, Gender, Marital_Status, Occupation, Monthly_Income,
       Educational_Qualifications, Family_size, latitude, longitude,
       Pin_code, Output):
    
    Prediction = classifier.predict([[Age, Gender, Marital_Status, Occupation, Monthly_Income,
       Educational_Qualifications, Family_size, latitude, longitude,
       Pin_code, Output]])
    
    print(Prediction)

    return "The Customer Feedback is " + str(Prediction)

def main():
    st.title("Online Food Customer Feedback")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit App</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    Age = st.text_input("Age")
    Gender = st.text_input("Gender")
    Marital_Status = st.text_input("Marital_Status")
    Occupation = st.text_input("Occupation")
    Monthly_Income= st.text_input("Monthly_Income")
    Educational_Qualifications = st.text_input("Educational_Qualifications")
    Family_size = st.text_input("Family_size")
    latitude = st.text_input("latitude")
    longitude = st.text_input("longitude")
    Pin_code = st.text_input("Pin_code")
    Output = st.text_input("Output")
    result = ""

    if st.button("Predict"):
        result = feedback(eval(Age), eval(Gender), eval(Marital_Status), eval(Occupation), eval(Monthly_Income),
       eval(Educational_Qualifications), eval(Family_size), eval(latitude), eval(longitude),
       eval(Pin_code), eval(Output))
    st.success("The Customer Feedback is : {}".format(result))
    if st.button("About"):
        st.text("Lets Learn ")
        st.text("It is about Online Food Customer Feedback")

if __name__ == "__main__":
    main()