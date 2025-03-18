#  Money Making mcahine app using Streamlit

import streamlit as st
import random
import time
import requests

# Set the title of the app
st.title("💰Money Making Machine💰")

#  side bar navigation
st.sidebar.title("💸 Money Zone 💸")
app_mode = st.sidebar.radio("Choose what you'd like to do:", ("Generate Money", "Side Hustle Ideas", "Money Quotes"))

# function to generate random amount of money

def generate_money():
    return random.randint(1,1000)

# function to fetch side hustles from Api

def fetch_side_hustles():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles?apikey=1234567890")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustles"]
        else:
            return {"Freelancing - Start offering your skills online!"}
    except:
        return {"something went wrong. Try again later."}
    
    # Function to fetch money quotes from API

def fetch_money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes?apikey=1234567890")
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quote"]
        else:
            return {"Money is a terrible master but an excellent servant."}
    except:
        return {"something went wrong. Try again later."}
    
    #  navigation logic

if app_mode == "Generate Money":
    st.subheader("💸 Instant Cash Generated 💸")
    if st.button("Tap to Generate Money!"):
       st.write("Counting your money.... 🤑")
       time.sleep(1)
       amount = generate_money()
       st.success(f"🎉 Congratulations! You made ${amount} 💵")

elif app_mode == "Side Hustle Ideas":
     st.subheader("💡 Side Hustle Ideas 💡")
     if st.button("Tap for Hustle Ideas!"):
        idea = fetch_side_hustles()
        st.success(idea) 

elif app_mode == "Money Quotes":
     st.subheader("💸 Motivational Money Quotes 💸")
     if st.button("Generate Money Quote"):
        quote = fetch_money_quotes()
        st.success(quote)             
