# DevOps Linux & Docker AI Assistant 🚀

A Streamlit-based web application that serves as an AI assistant for DevOps engineers and system administrators. It combines live system monitoring with interactive AI troubleshooting.

---

## ✨ Features

- **AI Chatbot:** Answers Linux, Docker, and DevOps troubleshooting queries using Groq API.
- **System Monitoring:** Displays real-time CPU, Memory, and system status metrics using `psutil`.
- **Voice Assistance:** Converts text responses to speech via ElevenLabs API.
- **Cloud Ready:** Configured for seamless deployment on AWS Elastic Beanstalk.

---

## 🛠️ Tech Stack

- **Frontend & Dashboard:** Streamlit
- **AI Core:** Groq API (LLM)
- **Voice Synthesis:** ElevenLabs API
- **System Metrics:** `psutil`
- **Deployment Platform:** AWS Elastic Beanstalk (Python 3.10 / Linux)

---

## ⚙️ Environment Variables

Set the following environment variables locally in a `.env` file or in AWS Elastic Beanstalk Environment Properties:

env
GROQ_API_KEY=your_groq_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key

## 🚀 Quick Start (Local Setup)
Clone the repository:

bash
git clone [https://github.com/Sumbulzahra/streamlit-devops-linux-ai-assistant.git](https://github.com/Sumbulzahra/streamlit-devops-linux-ai-assistant.git)
cd streamlit-devops-linux-ai-assistant

Create and activate a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
streamlit run app.py

---

## ☁️ Deployment on AWS Elastic Beanstalk
Ensure requirements.txt includes essential packages (streamlit, groq, elevenlabs, psutil, requests, python-dotenv).

Create a .zip archive of the project files (excluding venv/ and .env).

Deploy the .zip file on AWS Elastic Beanstalk Python environment.

Configure GROQ_API_KEY and ELEVENLABS_API_KEY in Configuration > Software > Environment properties.

## 📄 License
This project is licensed under the MIT License.
