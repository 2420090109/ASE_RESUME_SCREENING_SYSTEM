import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from extractor import extract_text
from ranker import rank_candidates

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/rank", methods=["POST"])
def rank():
    job_description = request.form.get("job_description", "")
    new_files = request.files.getlist("resumes")

    # 1. Save newly selected files (ignore empty submissions)
    for f in new_files:
        if f and f.filename.strip():
            filename = secure_filename(f.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            f.save(file_path)

    # 2. Extract and compile ALL existing files in the uploads folder
    resumes = []
    for filename in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.isfile(file_path) and (filename.endswith(".pdf") or filename.endswith(".docx")):
            text = extract_text(file_path)
            resumes.append({"name": filename, "text": text})

    if not resumes:
        return render_template("index.html", error="No resumes found to rank.")

    ranked = rank_candidates(job_description, resumes)
    return render_template("results.html", candidates=ranked, jd=job_description)

if __name__ == "__main__":
    app.run(debug=True)