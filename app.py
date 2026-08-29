import streamlit as st
import smtplib as mail
import wikipedia
import datetime 
from gtts import gTTS
from pathlib import Path

def speech(words):
    BASE_DIR = Path(__file__).resolve().parent
    audio_file = BASE_DIR / "speech.mp3"
    
    tts = gTTS(text=words, lang="en")    
    tts.save(str(audio_file))
    with st.expander("🔊 VOICE RESPONSE"):
        st.audio(str(audio_file))
        
st.markdown("""<h1 style='text-align: center'>VIRTUAL ASSISTANT</h1>""",unsafe_allow_html=True)
with st.sidebar:
    st.markdown("""
                <p style='font-family:Arial; font-size: 18px;'> <br> This is a simple Python based Virtual Assistant built with Streamlit that helps users perform useful daily tasks through Text commands. <br>
                Key Features:<br>
                1️⃣ Search on Wikipedia. <br>
                2️⃣ Send Email. <br>
                3️⃣ Open Websites. <br>
                © 2026 Muhammad Musab AlI.
                </p>""", unsafe_allow_html=True)
    
    speech(words=""" This is a simple Python based Virtual Assistant built with Streamlit that helps users perform useful daily tasks through text commands. 
                Key Features: such as Search on Wikipedia, Send Emails and Open Websites""")
    
    if st.button("DATE AND TIME"):
        strtime = datetime.datetime.now().strftime("%I:%M %p")
        strdate = datetime.datetime.now().strftime("%d/%m/%Y")
        st.write(F"TODAY IS {strdate}  &  TIME IS {strtime}")
        
    
def open_website():
    site = st.text_input("ENTER A WEBSITE").lower()
    if "youtube" in site:
        st.link_button("🌍 OPEN YOUTUBE","https://www.youtube.com")
    elif "google" in site:
        st.link_button("🌍 OPEN GOOGLE","https://www.google.com")
    elif "facebook" in site:
        st.link_button("🌍 OPEN FACEBOOK","https://www.facebook.com")
    elif "linkedin" in site:
        st.link_button("🌍 OPEN LINKEDIN","https://www.linkedin.com")


features = st.selectbox("HOW MAY I HELP YOU TODAY: ", ["SEARCH ON WIKIPEDIA",  "SEND EMAIL", "OPEN WEBSITE"])
if features=="SEARCH ON WIKIPEDIA":
    try:
        query = st.text_input("ENTER A QUERY TO SEARCH")
        results = wikipedia.summary(query, sentences=2).upper()
        st.write(results)
        speech(results)
    except Exception:
        st.warning("WAIT A SECOND")
    

elif features=="SEND EMAIL":
    email = st.text_input("ENTER YOUR EMAIL: ")
    password = st.text_input("ENTER PASSWORD: ", type="password")
    receiver = st.text_input("ENTER EMAIL OF RECEIVER: ")
    message = st.text_area("TYPE YOUR MESSAGE: ")
    if st.button("🎯 SEND EMAIL "):
        try:
            server = mail.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, receiver, message)
            server.close()
        except Exception:
            st.warning("NETWORK ISSUE")
            
else:
    open_website()
    
      
st.markdown("""
            <style>
            .block-container{
                padding-top: 2rem;
            }
            </style>
            """,unsafe_allow_html=True)
