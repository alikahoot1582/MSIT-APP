import streamlit as st
import numpy as np
from datetime import datetime
from uuid import uuid4
from PIL import Image

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="Fake News Detection Test",
    page_icon="🧠",
    layout="centered"
)

# ==================================================
# STYLING
# ==================================================
st.markdown("""
<style>
div[role="radiogroup"] > :first-child { display: none !important; }
.stRadio label { font-size: 17px; }
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

def fmt(x):
    return "Real" if x == "Real" else "Fake"

# ==================================================
# HEADER
# ==================================================
col1, col2 = st.columns([1, 3])
with col1:
    try:
        st.image(Image.open("logo.jpg"), width=120)
    except:
        pass

with col2:
    st.markdown("""
    ## 🧠 Fake News Detection Challenge  
    **Can you spot misinformation?**  
    Decide whether news headlines are *real* or *fake*.
    """)

# ==================================================
# ABOUT & FAQ
# ==================================================
with st.expander("📚 About this quiz"):
    st.markdown("""
    This quiz is inspired by the **Misinformation Susceptibility Test (MIST)**,
    a research-based method for understanding how people evaluate news credibility.

    Some headlines were generated using AI.
    """)

with st.expander("❓ FAQ"):
    st.markdown("""
    - Takes **2–5 minutes**
    - Open to users **13 years and older**
    - No names or emails collected
    - Educational and informational use only
    """)

# ==================================================
# CONSENT
# ==================================================
st.markdown("### 🔐 Participation")

consent = st.radio(
    "Do you agree to take this quiz anonymously?",
    ["", "Yes", "No"],
    horizontal=True
)

if consent == "":
    st.stop()

# ==================================================
# AGE GATE (13+ REQUIRED)
# ==================================================
st.markdown("### 🎂 Age Confirmation")

age_confirm = st.radio(
    "Are you 13 years or older?",
    ["", "Yes", "No"],
    horizontal=True
)

if age_confirm == "":
    st.stop()

if age_confirm == "No":
    st.error("Sorry — this experience is only available to users aged 13 or older.")
    st.stop()

# ==================================================
# SESSION INIT
# ==================================================
if "app_id" not in st.session_state:
    st.session_state.app_id = datetime.now().strftime('%Y%m%d-%H%M%S-') + str(uuid4())

# ==================================================
# TEST SELECTION
# ==================================================
st.markdown("### 🧪 Choose a Test Version")

test_choice = st.radio(
    "Select one:",
    ["", "MIST-20 (20 headlines)", "MIST-16 (16 headlines)"],
)

if test_choice == "":
    st.stop()

# ==================================================
# QUESTIONS
# ==================================================
if test_choice == "MIST-20 (20 headlines)":
    items = [
        "Government Officials Have Manipulated Stock Prices to Hide Scandals",
        "The Media Is Secretly Controlled by Major Corporations",
        "New Study: Eye Color Predicts Intelligence",
        "Vaccines Contain Dangerous Hidden Chemicals",
        "The Government Is Spreading Disease Through Technology",
        "Weather Is Being Artificially Controlled by Governments",
        "Ebola Was Caused by Weapons Testing",
        "Left-Wingers Are More Likely to Lie for Money",
        "Genetic Engineering Is Being Hidden from the Public",
        "UN Says Extremism Is Worse Than Terrorism",
        "Support for Legal Marijuana Remains Steady",
        "Young People Are More Concerned About Climate Change",
        "Hyatt Will Remove Small Bottles from Hotels",
        "America Is Less Respected Globally",
        "Democrats Support Science Funding More Than Republicans",
        "Republicans Are Divided on Trump",
        "Attitudes Toward the EU Are Largely Positive",
        "More Than One-Third Distrust NGOs",
        "US Counties Have Become More Diverse Since 2000",
        "Morocco Appoints Committee to Fight Poverty"
    ]
    labels = ["Fake"] * 10 + ["Real"] * 10

else:
    items = [
        "The Government Is Spreading Disease Through Technology",
        "A Small Group Controls the World Economy",
        "The Government Is Covering Up 9/11",
        "Left-Wingers Lie More for Better Grades",
        "Climate Science Is a Deceptive Method",
        "JFK Evidence Is Being Destroyed",
        "Hyatt Will Remove Small Bottles from Hotels",
        "US Hispanic Population Reached New High",
        "Large US Newspapers Laid Off Staff",
        "Most Americans Support Legal Abortion with Limits",
        "Athletes Speaking About Politics Is Accepted",
        "UN Receives Positive Global Approval",
        "Taiwan Joins Climate Fight",
        "Poverty Committee Appointed in Morocco",
        "Many Americans Distrust NGOs",
        "EU Support Remains Strong"
    ]
    labels = ["Fake"] * 8 + ["Real"] * 8

order = ["", "Real", "Fake"] if np.random.rand() < 0.5 else ["", "Fake", "Real"]
idx_order = np.random.permutation(len(items))

answers = []

with st.form("quiz_form"):
    st.markdown("## 📰 Headline Challenge")
    st.caption("Label each headline as REAL or FAKE")

    for i in idx_order:
        st.divider()
        answers.append(
            st.radio(items[i], order, format_func=fmt)
        )

    submit = st.form_submit_button("Submit")

# ==================================================
# RESULTS
# ==================================================
if submit and "" not in answers:
    score = sum(
        1 for i, idx in enumerate(idx_order)
        if answers[i] == labels[idx]
    )

    total = len(items)

    st.markdown("## 📊 Your Results")
    st.markdown(f"**Score:** {score} / {total}")

    if score >= total * 0.8:
        st.balloons()
        st.success("🎉 Excellent! You’re highly resistant to misinformation.")
    elif score >= total * 0.6:
        st.info("👍 Good job! Some room for improvement.")
    else:
        st.warning("⚠️ You may be vulnerable to misinformation.")

    st.caption("This result is for educational purposes only.")

# ==================================================
# FOOTER
# ==================================================
st.markdown("---")
st.markdown(
    "<div style='text-align:center; font-size:14px; opacity:0.7;'>"
    "🛠️ Made by <strong>Ali Kahoot</strong> · For ages <strong>13+</strong>"
    "</div>",
    unsafe_allow_html=True
)
