import streamlit as st
import joblib
import pandas as pd


model = joblib.load('attrition_model.pkl')
model_columns = joblib.load('model_columns.pkl')

st.title("Employee Attrition Prediction System (87.76% Accuracy) by Unni R")
st.write("Enter Employee details to predict Attrition trend.")


age = st.slider("Age", 18, 60, 30)
income = st.number_input("Monthly Income (Range Rs 1000 - 100000)", min_value=1000, max_value=100000, value=5000)
overtime = st.selectbox("Overtime", ["Yes", "No"])
job_level = st.slider("Job Level", 1, 5, 2)


if st.button("Predict"):
    
    data = pd.DataFrame([[age, income, job_level]], columns=['Age', 'MonthlyIncome', 'JobLevel'])
    
   
    for col in model_columns:
        if col not in data.columns:
            data[col] = 0
            
    prediction = model.predict(data[model_columns])[0]
    
    if prediction == 1:
        st.error("☹️ High Risk: This employee is likely to leave.")
    else:
        st.balloons()
        st.success("🙂 Low Risk: This employee is likely to stay.")
        
