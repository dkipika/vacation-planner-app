
import streamlit as st
import google.generativeai as genai
import os

# Load API Key from environment variable
api_key = st.secrets["GEMINI_API_KEY"]

# Check if API key is available
if not api_key:
    raise ValueError("⚠️ API Key not found! Set GEMINI_API_KEY in your environment variables.")

# Configure Google Gemini API
genai.configure(api_key=api_key)
# Load Model
model = genai.GenerativeModel("gemini-1.5-flash")

# Set page title
st.set_page_config(page_title="Vacation Planner", page_icon="🌍", layout="centered")

# Title
st.title("🌍 Vacation Planner App ✈️")

# Input fields
vd = st.text_input("Vacation Destination")
day = st.number_input("Number of Days", min_value=1, step=1)
bg = st.number_input("Budget (USD)", min_value=100, step=50)
ppl = st.number_input("Number of People", min_value=1, step=1)
sr = st.text_area("Specific Requirements (if any)")

# Ensure the destination is provided before generating a plan
if not vd:
    st.warning("Please enter a vacation destination.")

# Submit button
elif st.button("Generate Plan"):
    with st.spinner("Creating your vacation plan..."):
        prompt = f"Create a vacation plan for {ppl} people to {vd} for {day} days within a budget of {bg} USD. Specific requirements: {sr}."
        response = model.generate_content(prompt)

        if response and hasattr(response, "text"):
            st.subheader("✨ Your Vacation Plan ✨")
            st.write(response.text)
        else:
            st.error("Failed to generate a response. Please try again.")
