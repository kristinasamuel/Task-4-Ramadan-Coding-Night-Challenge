# Mood tracker app built with sretamlit python ,allowing users to log and visualize their emotional.

import streamlit as st  
import pandas as pd     
import datetime        
import csv        
import os                    

MOOD_FILE = "mood_log.csv"

def load_mood_data():
      # Check if file exists, if not, return an empty DataFrame
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date" , "Mood"])
    return pd.read_csv(MOOD_FILE)

def save_mood_data(date,mood):
    # Open the CSV file in append mode and write the date and mood
    with open(MOOD_FILE,"a") as file:
        writer = csv.writer(file)
        writer.writerow([date,mood])

# title of the app
st.title("👋 Welcome to the Mood Tracker App! 🎉")
today = datetime.date.today()

st.subheader("🎈 Let's Track Your Mood Journey Together! 💖")
mood = st.selectbox("select your mood",["Happy", "Sad", "Angry", "Neutral"])

# Log mood on button click
if st.button("log mood"):
    save_mood_data(today,mood)
    st.success("🎉 Mood Logged Successfully! ✅")

# Load and display mood trends
data = load_mood_data()
if not data.empty:
    st.subheader("🌈Your Mood Journey: Ups and Downs 📉")
    # Convert 'Date' to datetime format
    data["Date"] = pd.to_datetime(data["Date"])
    mood_counts = data.groupby("Mood").count()["Date"]
    st.bar_chart(mood_counts)

# Thanks message
st.write("✨ Thank you for using Mood Tracker! 💖")



