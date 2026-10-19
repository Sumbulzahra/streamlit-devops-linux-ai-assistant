# DevOps AI & Docker Assistant 🚀

An interactive Streamlit-based AI assistant designed to help DevOps engineers and system administrators monitor system performance, execute diagnostics, and query AI models (Groq) for quick technical insights and documentation.

---

## 🌟 Features

* **Interactive AI Chatbot:** Ask questions about Linux commands, Docker, CI/CD, and cloud infrastructures powered by Groq.
* **Real-time System Monitoring:** View live CPU usage, RAM utilization, and system status metrics.
* **Voice Integration:** Text-to-speech capabilities powered by ElevenLabs for voice assistance.
* **Cloud Ready:** Fully configured for seamless deployment on AWS Elastic Beanstalk.

---

## 🛠️ Tech Stack

* **Frontend & UI:** Streamlit
* **AI Engine:** Groq API / OpenAI SDK
* **Voice/Audio:** ElevenLabs SDK
* **System Metrics:** psutil, python-dotenv
* **Deployment:** AWS Elastic Beanstalk (Python / Linux)

---

## ⚙️ Environment Variables

To run this application locally or deploy it on AWS, you need to configure the following environment properties:

* `GROQ_API_KEY`: Your Groq API key
* `ELEVENLABS_API_KEY`: Your ElevenLabs API key

---

## 🚀 Local Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sumbulzahra/devops-ai-assistant.git](https://github.com/sumbulzahra/devops-ai-assistant.git)
   cd devops-ai-assistant
