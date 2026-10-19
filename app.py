import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from elevenlabs.client import ElevenLabs
from devops_monitor import get_complete_devops_context

# 1. Load Environment Variables from .env file
load_dotenv()

# 2. Get API Keys safely and remove hidden spaces/newlines
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if GROQ_API_KEY:
    GROQ_API_KEY = GROQ_API_KEY.strip()

ELEVENLABS_KEY = os.getenv("ELEVENLABS_KEY")
if ELEVENLABS_KEY:
    ELEVENLABS_KEY = ELEVENLABS_KEY.strip()

# DEBUG: Terminal mein check karne ke liye
print("DEBUG GROQ KEY:", GROQ_API_KEY)

# 3. Initialize Clients
groq_client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None
eleven_client = ElevenLabs(api_key=ELEVENLABS_KEY) if ELEVENLABS_KEY else None

# Page Configuration
st.set_page_config(page_title="DevOps AI Voice Assistant", page_icon="🤖", layout="wide")

st.title("🤖 DevOps Linux & Docker AI Assistant")
st.write("Apne system ki performance, Python version, aur Docker status ke baare mein poohein!")

# Sidebar for Live System Metrics
with st.sidebar:
    st.header("📊 Live System Stats")
    if st.button("Refresh Metrics"):
        st.rerun()
    
    # Get live metrics from monitoring module
    devops_info = get_complete_devops_context()
    st.text_area("[System & DevOps Environment State]", devops_info, height=350)

# Main Chat / Query Interface
st.subheader("💡 Assistant")
user_input = st.text_input(
    "Aap kya janna chahte hain? (e.g., 'python version batao' ya 'docker ps')",
    placeholder="Type your query here..."
)

if st.button("Ask AI") and user_input:
    if not GROQ_API_KEY:
        st.error("Groq API Key nahi mili! Kripya apni .env file check karein.")
    else:
        with st.spinner("AI response generate ho raha hai..."):
            try:
                # Prepare prompt with system context
                prompt = f"""
                You are an expert DevOps and Linux System Administrator AI Assistant.
                Here is the current live system context:
                {devops_info}

                User Question: {user_input}
                Provide a clear, helpful, and concise response.
                """
                
                # Fetch currently active models dynamically from Groq API
                available_models = [m.id for m in groq_client.models.list().data]
                
                response = None
                last_error = None

                # Loop through active models until one succeeds
                for model_name in available_models:
                    try:
                        response = groq_client.chat.completions.create(
                            model=model_name,
                            messages=[{"role": "user", "content": prompt}],
                            temperature=0.7
                        )
                        if response:
                            break
                    except Exception as err:
                        last_error = err
                        continue

                if response is None:
                    raise last_error if last_error else Exception("No active models found on Groq API.")

                ai_text = response.choices[0].message.content
                st.markdown("### 💡 Assistant Response:")
                st.write(ai_text)

                # Generate Audio via ElevenLabs Client
                if eleven_client:
                    try:
                        with st.spinner("🔊 Audio generation in progress..."):
                            audio_stream = eleven_client.text_to_speech.convert(
                                voice_id="JBFqnCBsd6RMkjVDRZzb",  # Rachel voice ID
                                text=ai_text[:300],
                                model_id="eleven_multilingual_v2"
                            )
                            audio_bytes = b"".join(chunk for chunk in audio_stream)
                            
                            if audio_bytes:
                                st.audio(audio_bytes, format="audio/mp3")
                            else:
                                st.warning("Audio stream empty thi.")
                    except Exception as e:
                        st.warning(f"Audio generation skipped: {e}")

            except Exception as e:
                st.error(f"Error generating response: {e}")
