# 📊 Sales Forecasting Application using XGBoost

## 📌 Introduction
This is my first GitHub project, focused on building a **machine learning–based sales forecasting system** using the **XGBoost regression model** and deploying it through an interactive **Streamlit web application**.

The project demonstrates how data science can be applied to solve real-world retail problems such as **sales prediction, demand planning, and business decision-making**.

---

## 🧠 Problem Statement
Retail stores need accurate sales forecasts to manage inventory, plan promotions, and optimize operations.  
Traditional methods often fail to capture complex patterns in sales data.

This project aims to:
- Predict future sales using machine learning
- Consider multiple business factors like promotions, holidays, and competition
- Provide an easy-to-use interface for predictions

---

## 📂 Dataset
- **Name:** Rossmann Store Sales Dataset
- **Source:** Kaggle
- **Type:** Structured tabular data
- **Target Variable:** `Sales`

## ⚙️ Machine Learning Model
- **Model Used:** XGBoost Regressor
- **Why XGBoost?**
  - Handles large datasets efficiently
  - Captures non-linear relationships
  - Performs well on structured business data

---

## 🧹 Feature Engineering
The model uses the following inputs:
- Store ID
- Day of Week
- Promotion status
- State holiday
- Store type
- Assortment level
- Competition distance
- Competition open date
- Promo interval
- Date-based features (Year, Month, Day)

Categorical variables are encoded before prediction.
---
## 🖥️ Web Application (Streamlit)
A **Streamlit-based web application** allows users to:
- Enter store and promotion details
- Select a forecasting date
- Get instant sales predictions

The application provides a simple and interactive UI suitable for non-technical users.

---

## 📊 Output
The model predicts the **expected sales value** for the selected store and date.

Example output:
Predicted Sales: 54,320.75

