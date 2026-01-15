import streamlit as st
import requests

# Page setup
st.set_page_config(page_title="Feedback", page_icon="📝")

# Replace 'YOUR_USERNAME' with your actual GitHub username below
GITHUB_USER = "suprabdullah96-collab" 
REPO_NAME = "for-my-valentine"

# Helper to get the correct GitHub image link
def get_image_url(filename):
    return f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/{filename}"

# Email function
def send_email(msg):
    url = "https://formsubmit.co/ajax/suprabdullah96@gmail.com"
    requests.post(url, json={"message": msg})

# 1. Bold Heading
st.markdown("# **You Don't Like My Previous Program?**")

# First Custom Photo (photo1)
# Make sure the extension matches (e.g., photo1.jpg or photo1.png)
st.image(get_image_url("photo1.jpg"))

# 2. Text Input Section
st.write("### Tell me what you like on IG")
user_input = st.text_input("Type your message here...", placeholder="I'd prefer if you...")

if st.button("Send to Abdullah"):
    if user_input:
        send_email(f"New Feedback: {user_input}")
        st.session_state.sent_feedback = True
        st.success("Message sent! ❤️")
    else:
        st.warning("Please type something before sending!")

# 3. Third Section: Appears only after sending
if st.session_state.get('sent_feedback'):
    st.divider()
    # Second Custom Photo (photo2)
    st.image(get_image_url("photo2.jpg"))
    st.balloons()
