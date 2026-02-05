IBM HR Analytics: Employee Attrition Prediction
Project Overview
This project aims to analyze the factors influencing employee attrition at IBM and build a predictive model to identify employees at risk of leaving. By combining Exploratory Data Analysis (EDA), SQL querying, and Machine Learning, we provide actionable insights for HR departments to improve retention rates.

Tech Stack
Language: Python 3.x

Libraries: Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn

Database: SQL

Deployment: Streamlit

Platform: GitHub & Streamlit Cloud

Key Findings (EDA)

Our analysis revealed several critical drivers of attrition:

Age: Significant turnover in the 25-35 age bracket.

Income: Lower salary levels are highly correlated with higher attrition.

Overtime: Employees working overtime are more likely to leave.

Job Role: Sales and Laboratory Technician roles show higher instability.

Machine Learning Model
We utilized a Random Forest Classifier to predict the likelihood of an employee leaving the organization.

Model Performance:
Accuracy: 87.76%

Evaluation Metrics: Precision, Recall, and F1-Score were used to ensure the model effectively identifies at-risk employees (minority class).

SQL Analysis
To handle large-scale data, SQL was used for segmented analysis:

SQL
-- Query to find Attrition rate by Department
SELECT Department, COUNT(Attrition) as Attrition_Count
FROM HR_Data
WHERE Attrition = 'Yes'
GROUP BY Department;

🌐 Live Application
The model has been deployed using Streamlit, allowing HR managers to input employee data and receive instant predictions.

🔗 [Link to Live App: https://hr-attrition-prediction-gzokkcffxtxvlrr6rdavgl.streamlit.app/]
