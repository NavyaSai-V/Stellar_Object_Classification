# Importing necessary libraries
import streamlit as st 
import pandas as pd
from joblib import load

# load joblib file as model
Model = load('XGBoost.joblib')

# Giving the title for the App
st.title("Stellar Object Classification App")

# Displaying the UI on the main screen
st.header("Enter the below details:")
alpha = st.number_input("Right Ascension angle: ")
delta = st.number_input("Declination angle: ")
u = st.number_input("Enter Ultraviolet filter value: ")
g = st.number_input("Enter green filter value:")
r = st.number_input("Enter Red filter value:")
i = st.number_input("Enter Near Infrared filter value:")
z = st.number_input("Enter Infrared filter value:")
cam_col = st.selectbox('Camera column', (1, 2, 3, 4, 5, 6))
redshift = st.number_input("Enter the redshift value: ")
plate = st.number_input("Enter the Plate ID:")
MJD = st.number_input("Enter the modified Julien Date: ")

prediction = Model.predict([[alpha, delta, u, g, r, i, z, cam_col, redshift, plate, MJD]])

st.header("Prediction Result")

if prediction[0] == 0:
    st.success("The object is a Galaxy")
elif prediction[0] == 1:
    st.success("The object is a Star")
else:
    st.success("the object is a QSO")