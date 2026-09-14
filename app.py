from flask import Flask, render_template, request
from pypdf import PdfReader
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Skills our application can detect
SKILLS = [
    "python",
    "java",
    "aws",
    "linux",
    "docker",
    "kubernetes",
    "terraform",
    "jenkins",
    "git",
    "github",
    "sql",
    "mysql",
    "flask",
    "html",
    "css",
    "javascript",
    "machine learning",
    "devops",
    "cloud computing"
]


def extract_resume_text(file):
    """Extract text from a PDF resume."""

    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text.lower()

    return text


def find_skills(text):
    """Find known skills in the given text."""

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills


@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    error = None

    if request.method == "POST":

        resume = request.files.get("resume")
        job_description = request.form.get(
            "job_description",
            ""
        )

        # Check resume
        if not resume or resume.filename == "":
            error = "Please upload a PDF resume."

            return render_template(
                "index.html",
                error=error
            )

        # Save resume
        resume_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            resume.filename
        )

        resume.save(resume_path)

        # Extract resume text
        resume_text = extract_resume_text(resume)

        # Find skills
        resume_skills = find_skills(resume_text)

        job_skills = find_skills(job_description)

        # Find matched skills
        matched_skills = list(
            set(resume_skills) &
            set(job_skills)
        )

        # Find missing skills
        missing_skills = list(
            set(job_skills) -
            set(resume_skills)
        )

        # Calculate percentage
        if job_skills:
            match_percentage = round(
                len(matched_skills)
                / len(job_skills)
                * 100
            )
        else:
            match_percentage = 0

        result = {
            "match_percentage": match_percentage,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills
        }

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)