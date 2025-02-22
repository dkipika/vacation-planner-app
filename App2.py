import streamlit as st
import google.generativeai as genai

# Configure Google Gemini API
genai.configure(api_key="AIzaSyCu4z-qehC3ndiTXa8G1AK983yyfx496d8")
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

# Submit button
if st.button("Generate Plan"):
    with st.spinner("Creating your vacation plan..."):
        prompt = f"Create a vacation plan for {ppl} people to {vd} for {day} days within a budget of {bg} USD. Specific requirements: {sr}."
        response = model.generate_content(prompt)
        
        # Display result
        st.subheader("✨ Your Vacation Plan ✨")
        st.write(response.text)
