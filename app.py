from flask import Flask, render_template, request
from pypdf import PdfReader
from docx import Document
from werkzeug.utils import secure_filename
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


# Recommended learning order for different skills
SKILL_RECOMMENDATIONS = {
    "python": "Improve Python programming and automation skills.",
    "java": "Learn Java fundamentals and object-oriented programming.",
    "aws": "Learn AWS core services such as EC2, S3, IAM, VPC and CloudWatch.",
    "linux": "Practice Linux commands, system administration and troubleshooting.",
    "docker": "Learn Docker images, containers, Dockerfiles and Docker Compose.",
    "kubernetes": "Learn Kubernetes pods, deployments, services and basic cluster management.",
    "terraform": "Learn Terraform infrastructure as code and AWS resource provisioning.",
    "jenkins": "Learn Jenkins pipelines and CI/CD automation.",
    "git": "Practice Git commands, branching, merging and version control.",
    "github": "Learn GitHub repositories, pull requests and collaboration workflows.",
    "sql": "Practice SQL queries, joins, filtering and database operations.",
    "mysql": "Learn MySQL databases, tables, queries and database management.",
    "flask": "Learn Flask routes, templates, forms and REST APIs.",
    "html": "Improve HTML structure, forms and semantic elements.",
    "css": "Improve CSS layouts, responsive design and styling.",
    "javascript": "Learn JavaScript fundamentals and browser interactions.",
    "machine learning": "Learn machine learning fundamentals and common algorithms.",
    "devops": "Learn CI/CD, Docker, cloud infrastructure and monitoring.",
    "cloud computing": "Learn cloud computing concepts and AWS fundamentals."
}


def extract_pdf_text(file_path):
    """Extract text from a PDF resume."""

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text.lower() + "\n"

    return text


def extract_docx_text(file_path):
    """Extract text from a DOCX resume."""

    document = Document(file_path)

    text = ""

    # Extract normal paragraphs
    for paragraph in document.paragraphs:
        if paragraph.text:
            text += paragraph.text.lower() + "\n"

    # Extract text from tables
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                if cell.text:
                    text += cell.text.lower() + "\n"

    return text


def extract_resume_text(file_path):
    """Extract text from PDF or DOCX resume."""

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_pdf_text(file_path)

    elif extension == ".docx":
        return extract_docx_text(file_path)

    else:
        raise ValueError("Unsupported file format")


def find_skills(text):
    """Find known skills in the given text."""

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills


def generate_recommendations(missing_skills):
    """Generate learning recommendations for missing skills."""

    recommendations = []

    for skill in missing_skills:

        recommendation = SKILL_RECOMMENDATIONS.get(skill)

        if recommendation:

            recommendations.append({
                "skill": skill,
                "recommendation": recommendation
            })

    return recommendations


@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    error = None

    if request.method == "POST":

        # Get uploaded resume
        resume = request.files.get("resume")

        # Get job description
        job_description = request.form.get(
            "job_description",
            ""
        )

        # Check resume
        if not resume or resume.filename == "":
            error = "Please upload a PDF or DOCX resume."

            return render_template(
                "index.html",
                error=error
            )

        # Check file type
        filename = secure_filename(resume.filename)

        extension = os.path.splitext(filename)[1].lower()

        allowed_extensions = [".pdf", ".docx"]

        if extension not in allowed_extensions:

            error = "Please upload a PDF or DOCX file only."

            return render_template(
                "index.html",
                error=error
            )

        # Save resume
        resume_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        resume.save(resume_path)

        try:

            # Extract resume text
            resume_text = extract_resume_text(
                resume_path
            )

            # Find skills in resume
            resume_skills = find_skills(
                resume_text
            )

            # Find skills in job description
            job_skills = find_skills(
                job_description
            )

            # Find matched skills
            matched_skills = sorted(
                list(
                    set(resume_skills)
                    & set(job_skills)
                )
            )

            # Find missing skills
            missing_skills = sorted(
                list(
                    set(job_skills)
                    - set(resume_skills)
                )
            )

            # Calculate match percentage
            if job_skills:

                match_percentage = round(
                    len(matched_skills)
                    / len(job_skills)
                    * 100
                )

            else:

                match_percentage = 0

            # Generate recommendations
            recommendations = generate_recommendations(
                missing_skills
            )

            # Determine match message
            if match_percentage >= 80:

                match_message = "Excellent Match!"

                match_description = (
                    "Your resume matches most of the "
                    "required skills for this job."
                )

            elif match_percentage >= 60:

                match_message = "Good Match!"

                match_description = (
                    "You have several relevant skills, "
                    "but there are some areas you can improve."
                )

            elif match_percentage >= 40:

                match_message = "Moderate Match"

                match_description = (
                    "You have some relevant skills, "
                    "but you should improve the missing skills."
                )

            else:

                match_message = "Needs Improvement"

                match_description = (
                    "Your resume has limited matching skills "
                    "for this job. Consider learning the missing skills."
                )

            result = {

                "match_percentage": match_percentage,

                "matched_skills": matched_skills,

                "missing_skills": missing_skills,

                "recommendations": recommendations,

                "match_message": match_message,

                "match_description": match_description

            }

        except Exception as e:

            error = (
                "Unable to analyze the resume. "
                "Please make sure the PDF or DOCX file is valid."
            )

            print("Error:", e)

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )