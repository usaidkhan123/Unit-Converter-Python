import streamlit as st


st.title("Unit Converter")

length_unit = {
    "Kilometers": 1000,  
    "Meters": 1,          
    "Centimeters": 0.01,  
    "Millimeters": 0.001, 
    "Miles": 1609.34,     
    "Yards": 0.9144,      
    "Feet": 0.3048,       
    "Inches": 0.0254      

}

weight_unit = {
    "Kilograms": 1,        
    "Grams": 0.001,        
    "Milligrams": 0.000001,
    "Pounds": 0.453592,    
    "Ounces": 0.0283495    
}

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return value


conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])


user_input = st.number_input("Enter value:", min_value=0.0, format="%.2f")

if conversion_type == "Length":
    from_unit = st.selectbox("From Unit", list(length_unit.keys()))
    to_unit = st.selectbox("To Unit", list(length_unit.keys()))
    if st.button("Convert"):
        if from_unit == to_unit:
            st.warning("Please select different units")
        else:
            result = user_input * (length_unit[to_unit] / length_unit[from_unit])
            st.success(f"{user_input} {from_unit} is equal to {result:.2f} {to_unit}")

elif conversion_type == "Weight":
    from_unit = st.selectbox("From Unit", list(weight_unit.keys()))
    to_unit = st.selectbox("To Unit", list(weight_unit.keys()))
    if st.button("Convert"):
        if from_unit == to_unit:
            st.warning("Please select different units")
        else:
            result = user_input * (weight_unit[to_unit] / weight_unit[from_unit])
            st.success(f"{user_input} {from_unit} is equal to {result:.2f} {to_unit}")

elif conversion_type == "Temperature":
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    if st.button("Convert"):
        if from_unit == to_unit:
            st.warning("Please select different units")
        else:
            result = convert_temperature(user_input, from_unit, to_unit)
            st.success(f"{user_input} {from_unit} is equal to {result:.2f} {to_unit}")
