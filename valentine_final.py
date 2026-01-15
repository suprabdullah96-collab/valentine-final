import streamlit as st
import requests

# Set page config
st.set_page_config(page_title="Valentine?", page_icon="❤️")

# Fix for the styling error
st.markdown("<style>.stButton button {width: 100%; border-radius: 20px;}</style>", unsafe_allow_html=True)

def send_email(msg):
    requests.post("https://formsubmit.co/ajax/suprabdullah96@gmail.com", json={"message": msg})

# Track progress
if 'stage' not in st.session_state: st.session_state.stage = 0
if 'phase2' not in st.session_state: st.session_state.phase2 = False

# PHASE 1: The Request
if not st.session_state.phase2 and st.session_state.stage < 100:
    st.title("Will you be my Valentine? 🌹")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHp1bmNid2Z4dzRieXp0eXpueXpueXpueXpueXpueXpueXpueXpueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/cLS1cfxvGOPVpf9g3y/giphy.gif")
    
    msgs = ["No", "Are you sure?", "Pookie please...", "Final chance!"]
    
    if st.session_state.stage < len(msgs):
        c1, c2 = st.columns(2)
        if c1.button("Yes"): st.session_state.stage = 100; st.rerun()
        if c2.button(msgs[st.session_state.stage]): st.session_state.stage += 1; st.rerun()
    else:
        if st.button("Maybe you don't like my previous program?"):
            st.session_state.phase2 = True; st.rerun()

# PHASE 2: The Feedback
elif st.session_state.phase2 and st.session_state.stage < 100:
    st.title("Maybe you don't like my previous program?")
    c1, c2 = st.columns(2)
    if c1.button("Yes, I don't like it"):
        send_email("She said she doesn't like the previous program")
        st.session_state.feedback = True
    if c2.button("No, I liked it"):
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHp1bmNid2Z4dzRieXp0eXpueXpueXpueXpueXpueXpueXpueXpueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/3o7TKoWXlo3S1Qfe6I/giphy.gif")
        st.success("Thanks! 🌸")

    if st.session_state.get('feedback'):
        txt = st.text_input("Tell What U Like")
        if st.button("Send"):
            send_email(f"What she likes: {txt}")
            st.session_state.stage = 100; st.rerun()

# FINAL SCREEN
if st.session_state.stage == 100:
    st.balloons()
    st.title("Thanks! Text me on IG! 📱")
    # Replace this URL with your 'photo2' link
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHp1bmNid2Z4dzRieXp0eXpueXpueXpueXpueXpueXpueXpueXpueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/K976VvCc8z4xG/giphy.gif")


