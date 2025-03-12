import streamlit as st

# Apply complete black background with white text and white title
st.markdown(
    """
    <style>
    body {
        background-color: #000000;  /* Complete black background */
        color: #ffffff;  /* White text */
    }
    .stApp {
        background-color: #000000;  /* Black background for the whole app */
    }
    h1 {
        color: #ffffff !important;  /* White title */
        text-align: center;
    }
    .stNumberInput, .stSelectbox, .stButton button {
        background-color: #333333; /* Dark grey input fields */
        color: white;
        border-radius: 5px;
        border: 1px solid white;
    }
    .stButton button {
        background-color: #ffffff;  /* White button */
        color: #000000;  /* Black text on button */
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #aaaaaa;  /* Light grey on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometer
        "kilometers_meters": 1000,   # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,    # 1 gram = 0.001 kilogram
        "kilograms_grams": 1000      # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}"  # Generate a key based on the input and output units
    return value * conversions[key] if key in conversions else "Conversion not supported"

# Title with white color
st.title("🔄 Unit Converter")

# User input fields
value = st.number_input("Enter the value:", min_value=0.0, value=0.0)
unit_from = st.selectbox("Convert From:", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("Convert To:", ["meters", "kilometers", "grams", "kilograms"])

# Convert button
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"**Converted Value:** `{result}`")
