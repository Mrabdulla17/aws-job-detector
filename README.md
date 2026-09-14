# AWS Job Detector 🚀

AWS Job Detector is a Python-based web application that analyzes a candidate's resume against a job description and identifies matching and missing skills.

The application helps job seekers understand how well their resume matches a particular job and which technical skills they may need to improve.

## 📌 Project Overview

The application allows users to:

- Upload a resume in PDF format
- Enter a job description
- Extract technical skills from the resume
- Compare resume skills with job requirements
- Calculate a resume-to-job match percentage
- Display matched skills
- Display missing skills
- Provide a simple and user-friendly web interface

## ✨ Features

### 📄 Resume Upload
Users can upload their resume as a PDF file.

### 🔍 Skill Detection
The application extracts relevant technical skills from the uploaded resume.

### 🎯 Job Matching
Resume skills are compared with the skills required by the job description.

### 📊 Match Percentage
The application calculates a percentage showing how closely the resume matches the job requirements.

### ✅ Matched Skills
Skills found in both the resume and job description are displayed.

### ❌ Missing Skills
Skills required by the job but missing from the resume are displayed.

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- PDF Processing
- Git
- GitHub
- AWS

## 📂 Project Structure

```text
aws-job-detector/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
└── uploads/