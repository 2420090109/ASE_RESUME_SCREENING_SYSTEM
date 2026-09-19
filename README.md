# AI-Based Resume Screening and Candidate Ranking System

Using DevSecOps and MLOps

An AI-powered system that automates the initial stage of recruitment by comparing resumes against job descriptions using NLP and machine learning — producing an objective, ranked candidate list with matched skills and key skill gaps.

---

## Overview

Recruiters often receive hundreds of applications for a single job opening. Manual screening is slow, inconsistent, and prone to human error. This project automates that first pass: it extracts skills, education, certifications, and experience from uploaded resumes, computes a relevance score against the job description using TF-IDF similarity, and returns a ranked shortlist — along with up to 2 key skill gaps per candidate to guide the recruiter's decision.

The project is built following Agile Scrum, with security integrated throughout via DevSecOps practices and experiment/model tracking via MLOps practices.

---

## Features

- 📄 Upload resumes in **PDF/DOCX** format alongside a job description
- 🧹 Automatic text extraction and preprocessing (skills, education, certifications, experience)
- 📊 **TF-IDF + cosine similarity** based relevance scoring
- 🏆 Ranked candidate list with **matched skills** and **up to 2 key skill gaps**
- 🌐 Simple web interface built with Flask
- 🔐 Security-first pipeline: static analysis, container scanning, dynamic testing
- 📈 Experiment tracking and monitoring hooks for reproducible ML

---

## Tech Stack

| Layer            | Technology                                   |
|-------------------|-----------------------------------------------|
| Language / ML      | Python, NLP, TF-IDF, scikit-learn             |
| Backend            | Flask                                          |
| Input              | PDF / DOCX resumes                             |
| Version Control    | Git, GitHub                                    |
| CI/CD              | GitHub Actions                                 |
| Deployment         | Docker, Kubernetes (Minikube)                  |
| Security           | SonarQube, Trivy, OWASP ZAP                   |
| MLOps              | DVC, MLflow                                    |
| Monitoring         | Prometheus, Grafana                            |

---

## Architecture / Workflow

```
Resume Upload → Text Extraction → Preprocessing → TF-IDF Vectorization
      → Similarity Scoring → Candidate Ranking → Recruiter Dashboard
```

---

## Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

```powershell
git clone https://github.com/<your-username>/resume-screening-system.git
cd resume-screening-system

python -m venv venv
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

### Running the app

```powershell
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

---

## Project Structure

```
resume-screening-system/
├── app.py                 # Flask application entry point
├── extractor.py           # Resume/JD text extraction + skill matching
├── ranker.py               # TF-IDF similarity scoring and ranking
├── requirements.txt
├── templates/
│   ├── index.html          # Upload form
│   └── results.html        # Ranked candidate output
└── static/
```

---

## Roadmap / Future Scope

- [ ] Extend ranking with **GitHub-based project evidence** — verify claimed skills using public repositories, languages, and project descriptions
- [ ] Explore semantic/BERT-based matching beyond TF-IDF
- [ ] Add fairness-aware ranking to reduce bias
- [ ] Full Kubernetes deployment with Prometheus/Grafana monitoring
- [ ] CI/CD pipeline with automated SonarQube, Trivy, and OWASP ZAP scans

---

## Team

| Name | Roll Number |
|---|---|
| Animesh Balaji Patro | 2420030301 |
| Navaneeth | 2420030306 |
| G. Satya Austin Abner | 2420030587 |
| Syed Musaib | 2420090109 |

**Guide:** Dr. Bhavya Varma Kalidindi
**Department of CSE** • Engineering Capstone Project – 1 • A.Y. 2026–2027

---

## License

This project is developed for academic purposes as part of the Engineering Capstone Project – 1 coursework.
