<a id="readme-top"></a>

<h1 align="center">Private RAG Chat Assistant LLM with Ollama Powered by Runpod Cloud</h1>

<div align="center">

**AI Chat Assistant**  
A private Retrieval-Augmented Generation (RAG) chatbot application using Ollama and LLMs, hosted on Runpod GPU cloud.

</div>

---

## 🚀 Quick Start

### 🔧 Prerequisites

Before starting, ensure you have the following installed/configured:

- Python 3.x
- [Ollama](https://ollama.com/)
- A Pod with GPU support created in [Runpod](https://www.runpod.io/)
- SSH access to your Runpod pod

---

## ⚙️ Setup Instructions

### 1. Create a Pod on Runpod

Go to [Runpod.io](https://www.runpod.io/) and set up a new pod with GPU support.

Choose the proper hardware and cost balance

Remember to Expose the HTTP Port 7860 (Do not use common port as 8501, 8080, 8888)

### 2. Connect to Your Pod

Use SSH to access your pod:

```bash
ssh your-username@your-pod-ip
```

### 3. Clone the repo

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 4. Run the application

```bash
streamlit run app.py \
  --server.address 0.0.0.0 \
  --server.port 7860 \
  --server.enableCORS false \
  --server.headless true \
  --server.enableWebsocketCompression false
```

---

### 🧠 Notes:

Ensure Ollama is running in the background before starting the application.

The app will be accessible from your browser using:

```bash
https://{POD_ID}-{INTERNAL_PORT}.proxy.runpod.net
```

### 🔄 Conversational History

The assistant now keeps the history of questions and answers within the same
session. This allows sending multiple sequential questions about the loaded
document without losing previous context.
