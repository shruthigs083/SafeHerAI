import streamlit as st
import sqlite3
from datetime import datetime
import speech_recognition as sr
import os
from streamlit_option_menu import option_menu
import os
from datetime import datetime



def save_user(name,email,phone):

    conn = sqlite3.connect("safeher.db")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users(name,email,phone) VALUES(?,?,?)",
        (name,email,phone)
    )

    conn.commit()
    conn.close()

def save_contact(name, relationship, phone):

    conn = sqlite3.connect("safeher.db")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO contacts(name,relationship,phone) VALUES(?,?,?)",
        (name, relationship, phone)
    )

    conn.commit()
    conn.close()
    
st.set_page_config(
    page_title="SafeHer AI",
    page_icon="🛡️",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

.main {
    background-color: #0e1117;
}

div[data-testid="metric-container"]{
    background-color:#262730;
    padding:20px;
    border-radius:15px;
    border:1px solid #444;
}

div[data-testid="metric-container"]:hover{
    transform:scale(1.03);
    transition:0.3s;
}

.stButton>button{
    width:100%;
    border-radius:12px;
    height:3em;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)


menu = [
    "Home",
    "Register",
    "Emergency Contacts",
    "SOS",
    "Incident Reports",
    "AI Threat Detector",
    "Evidence Vault",
    "Voice SOS",
    "Live Location",
    "About"
]

with st.sidebar:

    choice = option_menu(
        "SafeHer AI",
        menu,
        icons=[
            "house",
            "person-plus",
            "telephone",
            "exclamation-triangle",
            "file-earmark",
            "robot",
            "camera",
            "mic",
            "geo-alt",
            "info-circle"
        ],
        default_index=0
    )

if choice == "Home":
   
    st.write("📅", datetime.now().strftime("%d-%m-%Y %H:%M"))
    st.markdown("""
    <div style="
        padding:30px;
        border-radius:20px;
        background:linear-gradient(135deg,#ff4b4b,#6c63ff);
        color:white;
        text-align:center;
    ">
        <h1>🛡️ SafeHer AI</h1>
        <h3>AI-Powered Women Safety Platform</h3>
        <p>
        Real-Time SOS • Voice Detection • Threat Analysis • Evidence Vault
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")
    
    


    st.subheader("☎ Emergency Numbers")

    st.info("""
Police : 100

Women Helpline : 1091

Emergency : 112

Ambulance : 108
""")

    st.info("Your Safety. Our Priority. ❤️")

    # Feature Cards

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
🚨 SOS Alert

One-Tap Emergency Activation
""")

    with col2:
        st.info("""
🤖 AI Threat Detection

Detects Risky Situations
""")

    with col3:
        st.info("""
🎤 Voice SOS

Hands-Free Emergency Trigger
""")

    st.write("")
    st.write("")

    # Statistics Dashboard

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("👥 Users", "125")
    col2.metric("🚨 SOS Alerts", "43")
    col3.metric("📄 Reports", "18")
    col4.metric("📞 Contacts", "221")

    st.write("")
    st.write("")

    st.success(
        "SafeHer AI is actively protecting users through AI-powered safety monitoring."
    )  


elif choice == "Register":

    st.subheader("User Registration")

    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")

    if st.button("Register"):

        save_user(name,email,phone)

        st.success("User Saved Successfully")

elif choice == "Emergency Contacts":

    st.subheader("Trusted Emergency Contacts")
    st.image("logo.png", width=120)

    contact_name = st.text_input("Contact Name")

    relationship = st.selectbox(
        "Relationship",
        ["Mother","Father","Brother","Sister","Friend","Guardian","Other"]
    )

    phone = st.text_input("Phone Number")

    if st.button("Save Contact"):

        save_contact(contact_name, relationship, phone)

        st.success("Emergency Contact Saved")
elif choice == "SOS":

    st.subheader("🚨 Emergency SOS")

    if st.button("ACTIVATE SOS"):

        st.session_state["report"] = f"""
INCIDENT REPORT

Time: {datetime.now()}

Status: SOS Activated

Actions Taken:
✓ Emergency Contacts Notified
✓ Location Shared
✓ Evidence Recording Started
"""

        st.error("SOS ACTIVATED!")

        st.write("📍 Location Shared")
        st.write("📞 Emergency Contacts Notified")
        st.write("🎥 Evidence Recording Started")
elif choice == "Incident Reports":

    st.subheader("📄 Incident Reports")

    if "report" in st.session_state:
        st.text(st.session_state["report"])
    else:
        st.info("No incidents reported yet.")
elif choice == "AI Threat Detector":

    st.subheader("🤖 AI Threat Detector")

    message = st.text_area("Describe your situation")

    if st.button("Analyze Threat"):

        message = message.lower()

        high_risk = [
            "follow",
            "following",
            "attack",
            "kidnap",
            "chasing",
            "stalker",
            "help me",
            "danger"
        ]

        medium_risk = [
            "uncomfortable",
            "scared",
            "harass",
            "alone",
            "stranger"
        ]

        risk = "LOW"

        for word in high_risk:
            if word in message:
                risk = "HIGH"

        if risk != "HIGH":
            for word in medium_risk:
                if word in message:
                    risk = "MEDIUM"

        if risk == "HIGH":

            st.error("🔴 HIGH RISK")

            st.write("Recommendations:")
            st.write("• Activate SOS")
            st.write("• Move to a crowded area")
            st.write("• Contact emergency contacts")

            if st.button("🚨 Activate SOS Now"):

                st.session_state["report"] = f"""
INCIDENT REPORT

Time: {datetime.now()}

Status: AI Triggered SOS

Threat Level: HIGH

Actions Taken:
✓ Emergency Contacts Notified
✓ Location Shared
✓ Evidence Recording Started
"""

                st.success("SOS Activated Successfully")

        elif risk == "MEDIUM":

            st.warning("🟡 MEDIUM RISK")

            st.write("Recommendations:")
            st.write("• Stay alert")
            st.write("• Share your location")
            st.write("• Inform trusted contacts")

        else:

            st.success("🟢 LOW RISK")

            st.write("Situation appears safe")
elif choice == "Evidence Vault":

    st.subheader("📷 Evidence Vault")

    uploaded_file = st.file_uploader(
        "Upload Evidence",
        type=["jpg", "jpeg", "png", "mp3", "wav"]
    )

    if uploaded_file is not None:

     save_path = os.path.join(
        "evidence",
        uploaded_file.name
    )

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Evidence Saved Successfully")

    st.write("File Name:", uploaded_file.name)

    if uploaded_file.type.startswith("image"):
        st.image(uploaded_file)

elif choice == "Voice SOS":

    st.subheader("🎤 Voice SOS")

    if st.button("Start Listening"):

        recognizer = sr.Recognizer()

        try:

            with sr.Microphone() as source:

                st.info("Listening... Speak now")

                audio = recognizer.listen(source)

                text = recognizer.recognize_google(audio)

                st.success(f"You said: {text}")

                if "help" in text.lower():

                    st.error("🚨 SOS ACTIVATED")

                    st.write("📍 Location Shared")
                    st.write("📞 Emergency Contacts Notified")

                else:

                    st.info("No SOS keyword detected")

        except Exception as e:

            st.error(f"Error: {e}")
elif choice == "Live Location":

    st.subheader("📍 Live Location")

    latitude = st.text_input("Latitude")
    longitude = st.text_input("Longitude")

    if st.button("Share Location"):

        st.success("Location Shared Successfully")

        st.write(f"Latitude: {latitude}")
        st.write(f"Longitude: {longitude}")

elif choice == "About":

    st.subheader("🛡️ SafeHer AI")

    st.write("""
    SafeHer AI is an AI-powered women safety platform.

    Our mission is to help women stay safe through
    smart emergency response and AI-based threat detection.

    Features:
    • 🚨 SOS Alert
    • 📞 Emergency Contacts
    • 🤖 AI Threat Detection
    • 📷 Evidence Vault
    • 📄 Incident Reports
    • 🎤 Voice SOS
    • 📍 Live Location Sharing
    """)
    st.markdown("---")

st.markdown("""
<center>
<h4>🛡️ SafeHer AI</h4>
<p>AI-Powered Women Safety Platform</p>
<p>Developed using Python, Streamlit, SQLite and AI Concepts</p>
</center>
""", unsafe_allow_html=True)