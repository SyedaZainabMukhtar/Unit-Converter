#Project 01: Unit Convertor
#Build a Google Unit Convertor using Python and Streamlit:

import streamlit as st 
st.markdown(
    """
    <style>
    body{
        background-color: # 1e1e2f;
        color: white;
    }
    .stApp {
        background-color: linear-gradient(to right, #1e1e2f, #2a2a4f);
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 0 30px 0 rgba(0, 0, 0, 0.3);
    }
    h1{
        text-align: center;
        margin-bottom: 36px;
    }
    .stButton button{
        background: linear-gradient(45deg, #0b4636, #351c75);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }
    .stButton>button:hover{
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        box-align: center;ign: center;ign: center;ign: center;ign: center;ign: center;
        background: linear-gradient(45deg, #0b4636, #351c75);
        color: white;
    }
    .result{
        margin-top: 20px;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        color: #0b4636;
    }
    .result-box{
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer{
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: grey;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#title and description
st.markdown("<h1 style='text-align: center;'>Unit Convertor</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of measurement with our intuitive unit converter.")

#sidebar menu
conversion_type = st.sidebar.selectbox("Select conversion type:", ["Length", "Weight", "Temperature", "Volume"])
value = st.number_input("Enter the value to convert:", min_value=0.0, value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From:", ["Meters", "Kilometers", "Miles", "Feet", "Yards", "Inches"])
    with col2:
        to_unit = st.selectbox("To:", ["Meters", "Kilometers", "Miles", "Feet", "Yards", "Inches"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From:", ["Kilograms", "Grams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To:", ["Kilograms", "Grams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"])
elif conversion_type == "Volume":
    with col1:
        from_unit = st.selectbox("From:", ["Liters", "Gallons", "Cups", "Tablespoons", "Teaspoons"])
    with col2:
        to_unit = st.selectbox("To:", ["Liters", "Gallons", "Cups", "Tablespoons", "Teaspoons"])

#conversion logic
def length_conversion(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Miles": 0.000621371,
        "Feet": 3.28,
        "Yards": 1.09361,
        "Inches": 39.37,
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_conversion(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    temperature_units = {
        "Celsius": 1,
        "Fahrenheit": 1.8,
        "Kelvin": 1,
    }
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return value

##Button for conversion
if st.button("🔁Convert"):
    if value > 0:
        if conversion_type == "Length":
            result = length_conversion(value, from_unit, to_unit)
        elif conversion_type == "Weight":
            result = weight_conversion(value, from_unit, to_unit)
        elif conversion_type == "Temperature":
            result = temperature_conversion(value, from_unit, to_unit)
        
        st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
    else:
        st.error("Please enter a valid value to convert.")

#footer
st.markdown("<div class='footer'>Developed by SYEDA ZAINAB MUKHTAR</div>", unsafe_allow_html=True)

