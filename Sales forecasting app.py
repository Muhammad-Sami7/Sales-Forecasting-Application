import streamlit as st
import pandas as pd
import pickle
from datetime import datetime

# Load the trained model
with open('C:/Users/User/Desktop/Sales Forecasting/xgboost_rossmann.pkl', 'rb') as file:
    model = pickle.load(file)

# Page configuration
st.set_page_config(
    page_title="Sales Forecasting App",
    page_icon="📊",
    layout="wide",
)

# App Title
st.title("📈 Sales Forecasting Application")

# App Description
st.markdown("""
This application predicts the sales for stores based on user inputs. 
Please fill in the details below and click **Predict** to get the sales forecast.
""")

# Layout with 3 columns
col1, col2, col3 = st.columns(3)

# Inputs
with col1:
    store_id = st.number_input("🏬 Store ID", min_value=1, step=1, help="Enter the unique ID of the store")
    promo = st.selectbox("🎯 Promo", [0, 1], help="Whether the store is running a promo (1: Yes, 0: No)")
    state_holiday = st.selectbox("🏖️ State Holiday", ['0', 'a', 'b', 'c'], help="Type of state holiday (0: None, a/b/c: Types)")

with col2:
    date_input = st.date_input("📅 Select a Date", value=datetime.today(), help="Date for forecasting sales")
    store_type = st.selectbox("🏪 Store Type", ['a', 'b', 'c', 'd'], help="Category of the store")
    assortment = st.selectbox("📦 Assortment", ['a', 'b', 'c'], help="Level of product assortment")

with col3:
    competition_distance = st.number_input("📏 Competition Distance (meters)", min_value=0, step=1, help="Distance to nearest competitor")
    competition_open_since_month = st.slider("📆 Competition Open Since (Month)", 1, 12, value=1, help="Month when competitor opened")
    competition_open_since_year = st.number_input("📆 Competition Open Since (Year)", min_value=1900, value=2020, step=1, help="Year when competitor opened")
    promo_interval = st.text_input("📆 Promo Interval", value="", help="Promotion interval (e.g., Jan,Apr,Jul,Oct)")

# Extract Year, Month, Day from date
year = date_input.year
month = date_input.month
day = date_input.day

# Prepare input data
input_data = pd.DataFrame({
    'Store': [store_id],
    'DayOfWeek': [date_input.weekday() + 1],  # Convert to 1-7 scale
    'Open': [1],  # Assume store is open
    'Promo': [promo],
    'StateHoliday': [state_holiday],
    'SchoolHoliday': [0],  # Assume no school holiday; adjust if needed
    'StoreType': [store_type],
    'Assortment': [assortment],
    'CompetitionDistance': [competition_distance],
    'CompetitionOpenSinceMonth': [competition_open_since_month],
    'CompetitionOpenSinceYear': [competition_open_since_year],
    'Promo2': [0],  # Assume no Promo2; adjust if needed
    'Promo2SinceWeek': [0],
    'Promo2SinceYear': [0],
    'PromoInterval': [promo_interval],
    'Year': [year],
    'Month': [month],
    'Day': [day],
})

# Encoding function
def encode_data(data):
    """Encode categorical features into numeric format."""
    data['StateHoliday'] = data['StateHoliday'].astype('category').cat.codes
    data['StoreType'] = data['StoreType'].astype('category').cat.codes
    data['Assortment'] = data['Assortment'].astype('category').cat.codes
    data['PromoInterval'] = data['PromoInterval'].astype('category').cat.codes
    return data

# Encode input data
input_data = encode_data(input_data)

# Prediction Section
st.markdown("---")
st.header("📊 Prediction Results")

if st.button("Predict"):
    try:
        # Prediction
        prediction = model.predict(input_data)
        st.success(f"🌟 **Predicted Sales:** {prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"⚠️ An error occurred while predicting sales: {e}")
