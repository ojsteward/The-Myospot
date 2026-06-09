```python
   import streamlit as st

   st.title("🎈 The Myospot App")
   st.write("Welcome! This app is running completely from the cloud.")

   # A test widget
   user_input = st.text_input("What features are we building next?")
   if user_input:
       st.write(f"Awesome idea: **{user_input}**! We will code that soon.")