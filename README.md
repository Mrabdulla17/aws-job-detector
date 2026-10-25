# 🚀 AWS Job Detector

A Flask web app that compares a resume with a job description. It shows how well they match, which skills are present, which are missing, and generates a downloadable PDF report with learning suggestions.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)

## 🎯 What It Does

Job seekers often don't know how well their resume fits a role. This app answers that in seconds:

1. 📄 Upload your resume (PDF or DOCX)
2. 📝 Paste a job description
3. 📊 Get a match score, the skills you already have, and the skills you are missing
4. 📥 Download a PDF report with suggestions for each missing skill

## ✨ Features

- 📄 **Resume upload:** accepts `.pdf` and `.docx` files
- 🔍 **Skill detection:** finds technical skills in the resume and in the job description
- 🎯 **Job matching:** compares the two skill sets
- 📊 **Match percentage:** gives a score with a clear rating
  (Excellent, Good, Moderate or Needs Improvement)
- ✅ **Matched skills:** skills found in both
- ❌ **Missing skills:** skills the job asks for that the resume lacks
- 💡 **Recommendations:** a short suggestion for each missing skill
- 📥 **PDF report:** download the full analysis
- 🐳 **Docker support:** includes a Dockerfile

## 🧠 Skills It Looks For

Python, Java, AWS, Linux, Docker, Kubernetes, Terraform, Jenkins, Git, GitHub, SQL, MySQL, Flask, HTML, CSS, JavaScript, Machine Learning, DevOps, Cloud Computing.

The app uses keyword matching against this list. It does not use AI or call any AWS service.

## 🛠️ Tech Stack

| Area | Tools |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML5, CSS3 |
| File processing | pypdf (PDF), python-docx (DOCX) |
| Reports | ReportLab |
| Containers | Docker |
| Version control | Git, GitHub |

## 📁 Project Structure

```text
aws-job-detector/
├── app.py              # Flask app, skill matching, report generation
├── requirements.txt    # Python dependencies
├── Dockerfile          # container build
├── .dockerignore
├── .gitignore
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── screenshots/        # demo images used in this README
```

## 🚀 How to Run

### Option 1: With Python

```bash
git clone https://github.com/Mrabdulla17/aws-job-detector.git
cd aws-job-detector
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000 in your browser.

### Option 2: With Docker

```bash
git clone https://github.com/Mrabdulla17/aws-job-detector.git
cd aws-job-detector
docker build -t aws-job-detector .
docker run -p 5000:5000 aws-job-detector
```

Open http://localhost:5000 in your browser.

## 🔮 Future Improvements

- ☁️ Deploy on AWS (for example EC2) and add the live link here
- 🤖 Add a GitHub Actions workflow that builds the Docker image
- 🧠 Detect more skills and use smarter matching than keywords
- 🔒 Turn off Flask debug mode for production use

## 🎓 What I Learned

- Building a web app with Flask routes and HTML templates
- Reading text from PDF and DOCX files
- Generating PDF reports with ReportLab
- Packaging an app with Docker

## 👤 Author

**Abdulla G.** · [LinkedIn](https://www.linkedin.com/in/abdulla-g-bb7874340/) · [GitHub](https://github.com/Mrabdulla17)
