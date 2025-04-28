import streamlit as st
import streamlit_authenticator as stauth
from datetime import datetime
import random
from PIL import Image
import os

# ---- AUTHENTICATION ----
credentials_dict = {
    "usernames": {
        "growuser": {"name": "Green User", "password": "pass123"},
        "sponsor1": {"name": "Sponsor One", "password": "sponsorpass"}
    }
}

authenticator = stauth.Authenticate(
    credentials_dict, "growvertising_app", "abcdef", cookie_expiry_days=1
)

name, auth_status, username = authenticator.login("Login", "main")

if not auth_status:
    st.warning("Please log in to access the app.")
    st.stop()

st.sidebar.success(f"Welcome, {name}!")

# ---- HEADER ----
st.title("🌿 Growvertising – Billboard to Farmboard")
st.markdown("Turn every ad into action – grow plants, offset carbon, and join the green movement.")

# ---- BILLBOARD PREVIEW ----
st.subheader("🖼️ Billboard Preview")
billboards = {
    "Grow Your Greens": "https://i.imgur.com/U4A0lRQ.jpg",
    "From Message to Meal": "https://i.imgur.com/GQhuf0U.jpg",
    "Food Waste Awareness": "https://i.imgur.com/XY5NJJx.jpg"
}

selected_ad = st.selectbox("Select Campaign", list(billboards.keys()))
st.image(billboards[selected_ad], caption=selected_ad, use_column_width=True)

# ---- GROWTH SIM ----
st.subheader("🌱 Billboard Growth Status")
growth = st.slider("Simulated Growth Level (%)", 0, 100, 75)
st.progress(growth / 100)

# ---- COMMUNITY PHOTO WALL ----
st.subheader("📸 Upload Your Plant")
uploaded_file = st.file_uploader("Share your plant progress!", type=["jpg", "png"])
caption = st.text_input("Caption")

if uploaded_file and caption:
    # Save file locally for display
    img_path = f"temp_upload_{datetime.now().timestamp()}.jpg"
    with open(img_path, "wb") as f:
        f.write(uploaded_file.read())
    st.image(Image.open(img_path), caption=caption, use_column_width=True)
    st.success("Uploaded successfully!")

# ---- COMMENT WALL ----
st.subheader("💬 Comment Wall")
with st.form("comment_form"):
    comment = st.text_area("What's on your mind?", max_chars=250)
    if st.form_submit_button("Post") and comment:
        if "comments" not in st.session_state:
            st.session_state["comments"] = []
        st.session_state["comments"].append({
            "user": name,
            "comment": comment,
            "timestamp": str(datetime.now())
        })
        st.success("Comment posted!")

# Show recent comments
st.markdown("### Recent Comments:")
if "comments" in st.session_state:
    for entry in reversed(st.session_state["comments"][-5:]):
        st.markdown(f"**{entry['user']}** says: \n> {entry['comment']}")

# ---- BADGES ----
st.subheader("🏅 Your Grower Badge")
activity_score = random.randint(10, 100)
if activity_score > 80:
    badge = "🌟 Super Grower"
elif activity_score > 50:
    badge = "🌿 Urban Farmer"
else:
    badge = "🍀 Green Starter"

st.markdown(f"**Badge:** `{badge}`")
st.progress(activity_score / 100)

# ---- SPONSOR DASHBOARD ----
st.subheader("📊 Sponsor Dashboard")
st.metric("Total Plants Grown", "1,230 🌱", "+230 this week")
st.metric("CO₂ Offset", "420 kg", "+35 kg")
st.metric("Seed Kits Claimed", "890", "+102")
