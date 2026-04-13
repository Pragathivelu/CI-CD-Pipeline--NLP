# 🚀 AI Resume ATS Analyzer (NLP + BERT + T5 + CI/CD)

## 📌 Overview

This project is an **end-to-end AI-powered Applicant Tracking System (ATS)** that analyzes resumes against job descriptions and provides:

* ✅ Semantic skill matching
* 📊 ATS score (hybrid scoring)
* ❌ Missing skills identification
* 🤖 AI-generated professional feedback

The system leverages **modern NLP and deep learning models** along with **production-ready deployment (Docker + CI/CD)**.

---

## 🧠 Tech Stack

* **NLP & AI**

  * spaCy – Skill extraction
  * BERT (Sentence Transformers) – Semantic matching
  * T5 – Feedback generation

* **Backend**

  * FastAPI

* **Frontend**

  * Streamlit

* **DevOps**

  * Docker
  * GitHub Actions (CI/CD)

---

## 🏗️ Architecture

```
Resume + Job Description
        ↓
Text Cleaning
        ↓
Skill Extraction (spaCy)
        ↓
Skill Mapping (Ontology)
        ↓
Semantic Matching (BERT)
        ↓
Hybrid Scoring
        ↓
AI Feedback (T5)
        ↓
Final Output (Score + Skills + Suggestions)
```

---

## 📁 Project Structure

```
resume-ats-ai/
│
├── data/
│   └── ontology/
│       ├── skills.json
│       └── new_skills.json
│
├── src/
│   ├── preprocessing/
│   ├── nlp/
│   ├── features/
│   ├── matching/
│   ├── scoring/
│   ├── ontology/
│   └── pipeline/
│
├── api/
│   └── app.py
│
├── frontend/
│   └── streamlit_app.py
│
├── tests/
│   └── test_api.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .github/workflows/ci-cd.yml
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/resume-ats-ai.git
cd resume-ats-ai
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

---

## ▶️ Running the Application

### 🔥 Run Backend (FastAPI)

```bash
uvicorn api.app:app --reload
```

👉 Open Swagger UI:
http://127.0.0.1:8000/docs

---

### 🔥 Run Frontend (Streamlit)

```bash
streamlit run frontend/streamlit_app.py
```

---

## 🧪 API Usage

### Endpoint:

```
POST /analyze
```

### Sample Request:

```json
{
  "resume": "I have experience in Python and Machine Learning",
  "jd": "Looking for Python, SQL, Docker"
}
```

### Sample Response:

```json
{
  "ATS Score": 72.5,
  "Matched": ["python"],
  "Missing": ["sql", "docker"],
  "Feedback": "• Add SQL and Docker experience\n• Include measurable project impact\n• Improve project descriptions"
}
```

---

## 🐳 Docker Deployment

### Build Image

```bash
docker build -t ats-ai .
```

### Run Container

```bash
docker run -p 8000:8000 ats-ai
```

---

## ⚙️ CI/CD Pipeline (GitHub Actions)

This project includes a **CI/CD pipeline** that:

* ✅ Runs tests automatically
* 🐳 Builds Docker image
* 🚀 Pushes image to Docker Hub

### Required GitHub Secrets:

```
DOCKER_USERNAME
DOCKER_PASSWORD
```

---

## 🧠 Key Features

* 🔍 Intelligent skill extraction using NLP
* 🔗 Semantic matching using BERT
* 📊 Hybrid scoring system
* 🤖 AI-generated feedback using T5
* 🔄 Auto-updating skill ontology
* 🐳 Containerized deployment
* ⚙️ Automated CI/CD pipeline

---

## 🏆 Use Cases

* Resume screening systems
* Job portals
* HR automation tools
* Career guidance platforms

---
