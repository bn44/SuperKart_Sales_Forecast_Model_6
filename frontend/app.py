
import streamlit as st
import requests

#Base URL for the API
BACKEND_URL = "http://backend:7860"

st.title("SuperKart Sales Forecast Model") #Complete the code to define the title of the app.

# Input fields for product and store data
Product_Weight = st.number_input("Product Weight", min_value=0.0, value=12.66)
Product_Sugar_Content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
Product_Allocated_Area = st.number_input("Product Allocated Area", min_value=0.0, value=12.66)
Product_MRP = st.number_input("Product MRP", min_value=0.0, value=12.66)
Store_Size = st.number_input("Store Size", min_value=0.0, value=12.66)
Store_Location_City_Type = st.selectbox("Store Location City Type", ["Rural", "Semi-Urban", "Urban"])
Store_Type = st.selectbox("Store Type", ["Small", "Medium", "Large"])
Product_Id_char = st.text_input("Product ID")
Store_Age_Years = st.number_input("Store Age Years", min_value=0.0, value=12.66)
Product_Type_Category = st.selectbox("Product Type Category", ["Fruits", "Vegetables", "Dairy"])

product_data = {
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_MRP": Product_MRP,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Product_Id_char": Product_Id_char,
    "Store_Age_Years": Store_Age_Years,
    "Product_Type_Category": Product_Type_Category
}

if st.button("Predict", type='primary'):
    response = requests.post("http://{BACKEND_URL}/v1/predict", json=product_data) # Send data to Flask API
    if response.status_code == 200:
        result = response.json()
        predicted_sales = result["Sales"]
        st.write(f"Predicted Product Store Sales Total: ${predicted_sales:.2f}")
    else:
        st.error("Error in API request")
