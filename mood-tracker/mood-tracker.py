import streamlit as st  # Web interface
import pandas as pd  # Data manipulation
import datetime  # Date handling
import csv  # CSV file operations
import os  # File operations

# File name for storing mood data
Mood_File = "mood_log.csv"

# Function to load mood data from CSV
def load_mood_data():
    if not os.path.exists(Mood_File):
        return pd.DataFrame(columns=["Date", "Mood"])  # Return empty DataFrame if file doesn't exist
    return pd.read_csv(Mood_File)

# Function to save mood data
def save_mood_data(date, mood):
    file_exists = os.path.exists(Mood_File)
    
    with open(Mood_File, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Mood"])  # Write headers if the file is new
        writer.writerow([date, mood])

# Streamlit UI
st.title("📅 Mood Tracker")

today = datetime.date.today().strftime("%Y-%m-%d")  # Convert date to string
st.subheader("How are your feelings today?")

# Mood selection dropdown
mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Stressed", "Anxious", "Excited", "Neutral", "Tired"])

# Button to log mood
if st.button("Log Mood"):
    save_mood_data(today, mood)
    st.success(f"✅ Mood logged successfully for {today}!")

# Load and display mood data
data = load_mood_data()

if not data.empty:
    st.subheader("📊 Mood Trends Over Time")

    # Convert 'Date' column to datetime format
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")

    # Check for valid dates
    if data["Date"].notna().any():
        mood_counts = data["Mood"].value_counts()
        
        # Display mood counts as a bar chart
        st.bar_chart(mood_counts)

    # Show the raw mood data in a table
    st.subheader("📜 Logged Mood Data")
    st.dataframe(data)

else:
    st.warning("No mood data found. Log your mood to see trends!")

