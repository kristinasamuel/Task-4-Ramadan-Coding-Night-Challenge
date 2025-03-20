# Time zone app display the current time in multiple time zones and convert time between time zones.

import streamlit as st 
from datetime import datetime
from zoneinfo import ZoneInfo

# List of available time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "Asia/Dubai",
    "Asia/kolkata",
    "America/New_York",
    "Europe/London",
    "Australia/Sydney",
    "Europe/Paris",
]

# title of the app
st.title("🌍 Time Zone App 🧭")
# Allow users to select multiple time zones
selected_time_zone = st.multiselect("Select Time Zones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

# Display the selected time zones and their current time
st.subheader("🕒 Current Time in Selected Time Zones")
for tz in selected_time_zone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y:%m:%d %I:%M:%S %p")
    st.write(f"**{tz}** : {current_time}")

# Convert time between time zones
st.subheader("🔄 Convert Time Between Time Zones")
current_time = st.time_input("current Time", value=datetime.now().time())
from_tz = st.selectbox("From Time Zone", TIME_ZONES,index=0)   
to_tz = st.selectbox("To Time Zone",TIME_ZONES,index=1)
if st.button("Convert time"):
    dt = datetime.combine(datetime.today(),current_time,tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y:%m:%d %I:%M:%S %p")
    st.success(f"✅ **Converted Time** in {to_tz} : {converted_time} ⏳")

