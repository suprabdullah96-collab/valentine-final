import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="For You ❤️", page_icon="🌹")

# 2. Custom Styling
st.markdown("""
    <style>
    .stButton button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

if 'stage' not in st.session_state:
    st.session_state.stage = "game"
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0

# --- PART 1: THE GAME ---
if st.session_state.stage == "game":
    st.title("Will you be my Valentine? 🌹")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHp1bmNid2Z4dzRieXp0eXpueXpueXpueXpueXpueXpueXpueXpueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/cLS1cfxvGOPVpf9g3y/giphy.gif")
    
    messages = ["No", "Are you sure?", "Pookie please...", "Don't do this...", "I'll be sad...", "Only 'Yes' left!"]
    
    if st.session_state.no_count < len(messages) - 1:
        col1, col2 = st.columns([1, 1])
        with col1:
            yes_label = "Yes" + ("!" * st.session_state.no_count)
            if st.button(yes_label, key="yes_g"):
                st.session_state.stage = "success"
                st.rerun()
        with col2:
            if st.button(messages[st.session_state.no_count], key="no_g"):
                st.session_state.no_count += 1
                st.rerun()
    else:
        if st.button("YES! ❤️", key="final_yes"):
            st.session_state.stage = "success"
            st.rerun()
        st.write("---")
        if st.button("Maybe you don't like this? Click here ⮕", key="to_plan_b"):
            st.session_state.stage = "plan_b_1"
            st.rerun()

# --- PART 2: SUCCESS SCREEN ---
elif st.session_state.stage == "success":
    st.balloons()
    st.title("Knew you would say yes! ❤️")
    st.subheader("We'll ride horses together! ")
    try:
        st.image("photo2.jpg")
    except:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHp1bmNid2Z4dzRieXp0eXpueXpueXpueXpueXpueXpueXpueXpueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/K976VvCc8z4xG/giphy.gif")
    st.write("Talk to you on IG! ")

# --- PART 3: PLAN B (EMAIL REDIRECT) ---
elif st.session_state.stage == "plan_b_1":
    st.title("Maybe u don't like the previous program... 😅")
    try:
        st.image("photo1.jpg")
    except:
        st.info("Upload 'photo1.jpg' to GitHub to see your photo here!")
    if st.button("Next ➡️"):
        st.session_state.stage = "plan_b_2"
        st.rerun()

elif st.session_state.stage == "plan_b_2":
    st.title("I want to make it better! ✨")
    st.subheader("Tell me what do you like on IG?")
    ans = st.text_area("Type here...", placeholder="Tell me what you enjoy and we'll do in ur city...")
    
    if st.button("Send Message 💌"):
        if ans:
            # YOUR ACTUAL EMAIL ADDED HERE
            your_email = "suprabdullah96@gmail.com" 
            subject = "Valentine Response"
            url = f"https://formsubmit.co/el/{your_email}?subject={subject}&message={ans}"
            
            st.markdown(f'''
                <a href="{url}" target="_self" style="text-decoration: none;">
                    <button style="width:100%; border-radius:20px; background-color:#ff4b4b; color:white; height:3em; border:none; font-weight:bold; cursor:pointer;">
                        Final Step: Click to Confirm Send! ❤️
                    </button>
                </a>
            ''', unsafe_allow_html=True)

