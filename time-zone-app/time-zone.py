import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

Time_Zone = [
    "UTC",
    "Asia/Shanghai",
    "Asia/Hong_Kong",
    "Asia/Seoul",
    "Asia/Dubai",
    "Africa/Cairo",
    "Asia/Karachi",
    "America/New_York",
    "America/Los_Angeles",
    "America/Chicago",
    "Europe/London",
    "Europe/Paris",
    "Asia/Taipei",
    "Asia/Karachi",
]

st.title("🕰️Time Zone app")

selected_time_zone = st.multiselect("Select a time zone", Time_Zone, default=["UTC" ,"Asia/Karachi"])

st.subheader("Current Time")

for time_zone in selected_time_zone:
    current_time = datetime.now(ZoneInfo(time_zone)).strftime('%Y-%m-%d %I %H:%M:%S %p')
    st.write(f"{time_zone}: {current_time}")

st.subheader("Convert Time Between Timezones")

current_time = st.time_input("Current Time", value=datetime.now().time())

from_time_zone = st.selectbox("From Timezone", Time_Zone, index=0)

to_time_zone = st.selectbox("To Timezone", Time_Zone, index=1)

if st.button("Convert Time"):

    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_time_zone))

    converted_time = dt.astimezone(ZoneInfo(to_time_zone)).strftime('%Y-%m-%d %I %H:%M:%S %p')

    st.success(f"Converted Time in {to_time_zone}: {converted_time}")



