import streamlit as st
import requests


# Function to fetch a random quote from Forismatic API
def get_quote():
    url = "http://api.forismatic.com/api/1.0/"
    params = {
        "method": "getQuote",
        "format": "json",
        "lang": "en"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['quoteText'], data['quoteAuthor']


# App Layout
st.write("Quote of the Day 🌟")

try:
    # Fetch quote
    quote, author = get_quote()
    # Display quote
    st.write(f"\"{quote}\"")
    # Display author
    st.write(f"👤 {author}")

except Exception:
    st.write("No quotes today 😵‍💫")

# Display app version
st.write("App Version: v0.1")
